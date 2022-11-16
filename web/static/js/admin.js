localAddress = 'http://127.0.0.1:5500';

function CookieSet(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                console.log(cookieValue);
                if (cookieValue == 'administrator') {
                    return true;
                }
            }
        }
        return false;
    }
}

$( document ).ready(function() {
    console.log( "ready!" );
    //accept only administrator
    if (!CookieSet('user_role')) {
        window.location.href = localAddress + '/templates/401.html';
    }
});
