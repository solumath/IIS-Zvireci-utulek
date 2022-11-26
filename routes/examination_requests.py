import response as r
from app import app
import flask
import flask_login
import db
import utility
import datetime
from munch import DefaultMunch


# @app.route("/examinations/request", methods=["POST"])
# @flask_login.login_required
# def examination_requests_add():
#     if flask.request.method == "POST":
#         form = flask.request.form
#         try:
#             animal = db.get_animal(form["animal"])
#             user = db.get_user(form["user"])
#             date = form["date"]
#             start = utility.datetime_from_date(date, "08:00")
#             end = utility.datetime_from_date(date, "18:00")
#             request = form["request"]
#         except:
#             flask.flash(r.UNSPECIFIEDDefaultMunch_ERROR, r.ERROR)
#             return flask.redirect("/")

#         if start < datetime.datetime.now():
#             flask.flash(r.PLANNING_HISTORY, r.ERROR)
#             return flask.redirect(flask.url_for("animal_detail", id=animal.id))

#         new_request = db.ExaminationRequest(start, end, request)
#         new_request.user = user
#         new_request.animal = animal
#         db.db.session.add(new_request)
#         db.db.session.commit()

#     flask.flash(r.REQUEST_SUCCEED, r.OK)
#     return flask.redirect(flask.url_for("animal_detail", id=animal.id))


@app.route("/examinations/accept/<id>", methods=["GET", "POST"])
@flask_login.login_required
def examination_requests_accept(id):
    request = db.get_examination_request(id)
    if request is None:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect(flask.url_for("examination_requests"))

    if flask.request.method == "POST":
        form = flask.request.form
        try:
            request_form = DefaultMunch.fromDict(form)
            start = utility.parse_html_datetime(form["start"])
            end = utility.parse_html_datetime(form["end"])
            request_desc = form["request"]
        except:
            flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
            return utility.render_with_permissions("examination_request_accept.html", request=request_form, animal=request.animal)

        request.start = start
        request.end = end
        request.request = request_desc
        request.accepted = True
        db.db.session.commit()
        return flask.redirect(flask.url_for("examination_requests"))

    return utility.render_with_permissions("examination_request_accept.html", request=request, animal=request.animal)


@app.route("/examinations/decline/<id>", methods=["GET"])
@flask_login.login_required
def examination_requests_decline(id):
    request = db.get_examination_request(id)
    if request is None:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect(flask.url_for("examination_requests"))

    db.db.session.delete(request)
    db.db.session.commit()

    return flask.redirect(flask.url_for("examination_requests"))


@app.route("/examinations/delete/<id>", methods=["GET"])
@flask_login.login_required
def examination_requests_delete(id):
    request = db.get_examination_request(id)
    if request is None:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect(flask.url_for("medical_records"))

    db.db.session.delete(request)
    db.db.session.commit()

    return flask.redirect(flask.url_for("medical_records"))


@app.route("/examinations/perform/<id>", methods=["GET", "POST"])
@flask_login.login_required
def examination_requests_perform(id):
    request = db.get_examination_request(id)
    if request is None:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect(flask.url_for("examination_requests"))

    if flask.request.method == "POST":
        form = flask.request.form
        try:
            assert request.accepted == True
            request_form = DefaultMunch.fromDict(form)
            request_desc = form["request"]
        except:
            flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
            return utility.render_with_permissions("examination_request_perform.html", request=request_form, animal=request.animal)

        record = db.MedicalRecord(request.start, request.end, request_desc)

        db.db.session.delete(request)
        db.db.session.add(record)
        record.animal = request.animal
        record.user = request.user
        record.record_type = db.get_record_type("examination")
        db.db.session.commit()
        return flask.redirect(flask.url_for("examination_requests"))

    return utility.render_with_permissions("examination_request_perform.html", request=request, animal=request.animal)


@app.route("/examinations")
@flask_login.login_required
def examination_requests():
    requests = db.get_examination_requests(
        user=flask_login.current_user, accepted=False)
    accepted = db.get_examination_requests(
        user=flask_login.current_user, accepted=True)
    return utility.render_with_permissions("examination_requests.html", requests=requests, accepted=accepted)
