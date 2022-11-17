localAddress = 'http://127.0.0.1:5500';

function CookieSet(name) {
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                return true;
            }
        }
        return false;
    }
}

$( document ).ready(function() {
    console.log( "ready!" );

    //if user is not logged in, redirect to 401.html
    if (!CookieSet('token')) {
        window.location.href = localAddress + '/html/401.html';
    }

});
