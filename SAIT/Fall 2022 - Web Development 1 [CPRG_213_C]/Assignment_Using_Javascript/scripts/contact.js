// when the "submit-button" is clicked, the contents of the contact-page are replaced with a single <p> element that reads "Thank you for your message" in size 24 font.

// hint: you can change the style of an element by modifying the value of that element's .style.fontSize, or by updating its .classList.

var SUBBUTT = document.getElementById("submit-button");

function SUB() {

    const p = document.createElement("p");
    p.innerHTML = "THANK YOU FOR YOUR MESSAGE!";

    var INFO = document.getElementById("contact-page");
    INFO.replaceWith(p);
}

if (SUBBUTT) {
    SUBBUTT.addEventListener("click", SUB);
}