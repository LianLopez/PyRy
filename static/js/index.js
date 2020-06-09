


// DOM EVENTS

document.getElementById("menuIcon").addEventListener("click", display);
var menu = true;
function display() {
    if (menu) {
        menu = false;
        document.getElementById("menuIcon").classList.remove("fa-bars");
        document.getElementById("menuIcon").classList.add("fa-remove");
    } else {
        menu = true;
        document
            .getElementById("menuIcon")
            .classList.remove("fa-remove");
        document.getElementById("menuIcon").classList.add("fa-bars");
    }
}