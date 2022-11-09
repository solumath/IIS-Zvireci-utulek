// https://www.youtube.com/watch?v=RVrHC__Tkx0&ab_channel=ABNationProgrammers
// fce slouzici k filtrovani karet pomoci titulku
function filtering() {
    const input = document.getElementById("filtering").value.toUpperCase();
    const cardContainer = document.getElementById("animals");
    const cards = cardContainer.getElementsByClassName("column");
    for (let i = 0; i < cards.length; i++) {
        let title = cards[i].getElementsByClassName("card")[0].querySelector(".card-body h2.card-title");
        if (title.innerText.toUpperCase().indexOf(input) > -1) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    }
}
