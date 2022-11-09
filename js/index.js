$( document ).ready(function(e) {
    console.log( "ready!" );

    // load footer and navbar
    $("#footer-placeholder").load("../html/footer.html");
    $("#navbar-placeholder").load("../html/navbar.html");
});
