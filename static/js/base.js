$( document ).ready(function() {
    if ($("#flashes *").length > 0) {
        $("#modalId").modal('show');
    }
});

function closeModalWindow(modal) {
    $(modal).modal('hide');
}

$(document).on('keydown', function() {
    closeModalWindow('#modalId');
});
