// when the "submit-button" is clicked, the contents of the contact-page are replaced with a single <p> element that reads "Thank you for your message" in size 24 font.

// hint: you can change the style of an element by modifying the value of that element's .style.fontSize, or by updating its .classList.

var SUBBUTT = document.getElementById("submit-button"); 
SUBBUTT.addEventListener("click", SUB);

function SUB()

{

    console.log("Submit Attempted");
    document.getElementsByTagName("main")[0].innerHTML = "<p>THANK YOU FOR YOUR MESSAGE!</p>";
    document.getElementsByTagName("p")[0].style.fontSize = "24px";

}

// var SUBBUTT = document.getElementById("submit-button");

// function SUB() {

//     const p = document.createElement("p");SUBBUTT.addEvent
//     p.innerHTML = "THANK YOU FOR YOUR MESSAGE!";
//     p.classList.add("contact")

//     var INFO = document.getElementById("contact-page");
//     INFO.replaceWith(p);
// }

// if (SUBBUTT) {
//     SUBBUTT.addEventListener("click", SUB);
// }