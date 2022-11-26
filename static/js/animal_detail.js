$( document ).ready(function() {
    console.log( "ready!" );

    $('.walksTable').DataTable();
});

function showAndHide() {
    var x = document.getElementById("walks_detail");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
