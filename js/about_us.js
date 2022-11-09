$( document ).ready(function() {
    console.log( "ready!" );

    // load footer and navbar
    $("#footer-placeholder").load("../html/footer.html");
    $("#navbar-placeholder").load("../html/navbar.html");
});
