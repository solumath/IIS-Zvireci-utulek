from app import app
import utility


@app.route('/')
def index():
    return utility.render_with_permissions('index.html')


@app.route('/about')
def about():
    return utility.render_with_permissions('about.html')


@app.errorhandler(401)
def not_enough_perms(e):
    return utility.render_with_permissions('401.html')


@app.errorhandler(404)
def page_not_found(e):
    return utility.render_with_permissions('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return utility.render_with_permissions('500.html')
