/********* create variables *********/
// useful variables might be: the cost per day, the number of days selected, and elements on the screen that will be clicked or will need to be modified. 
// Do any of these variables need to be initialized when the page is loaded? 
// When do they need to be reset or updated?

var CPD; //Cost Per Day
var NODS; //Number of Days Selected
var PRATE; //Price Rate
var T; //Total Cost
var C_Button = document.getElementById("clear-button") //To Reset Button Contents

//Variables for Weekdays 
var MON =  document.getElementById("monday"); 
var TUE =  document.getElementById("tuesday");
var WED =  document.getElementById("wednesday");
var THUR =  document.getElementById("thursday");
var FRI =  document.getElementById("friday");

//Variables for Amount of the Day
var FULL = document.getElementById("full");
var HALF = document.getElementById("half");

/********* colour change days of week *********/
// when the day buttons are clicked, we will apply the "clicked" class to that element, and update any other relevant variables. Then, we can recalculate the total cost.
// added challenge: don't update the dayCounter if the same day is clicked more than once. hint: .classList.contains() might be helpful here!

function update(button) {
    button.classList.add("clicked");
    days += 1;
    recalculate();
}

if (monday) {
    monday.addEventListener("click", update.bind(null, monday));
}

if (tuesday) {
    tuesday.addEventListener("click", update.bind(null, tuesday));
}

if (wednesday) {
    wednesday.addEventListener("click", update.bind(null, wednesday));
}

if (thursday) {
    thursday.addEventListener("click", update.bind(null, thursday));
}

if (friday) {
    friday.addEventListener("click", update.bind(null, friday));
}



/********* clear days *********/
// when the clear-button is clicked, the "clicked" class is removed from all days, any other relevant variables are reset, and the calculated cost is set to 0.


function clear() {
    monday.classList.remove("clicked");
    tuesday.classList.remove("clicked");
    wednesday.classList.remove("clicked");
    thursday.classList.remove("clicked");
    friday.classList.remove("clicked");
    days = 0;
    total = 0;
    setFull();
}

if (clearButton) {
    clearButton.addEventListener("click", clear);
}



/********* change rate *********/
// when the half-day button is clicked, set the daily rate to $20, add the "clicked" class to the "half" element, remove it from the "full" element, and recalculate the total cost.

function setHalf() {
    rate = 20;
    half.classList.add("clicked");
    full.classList.remove("clicked");
    recalculate();
}

if (half) {
    half.addEventListener("click", setHalf);
}

// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.

function setFull() {
    rate = 35;
    full.classList.add("clicked");
    half.classList.remove("clicked");
    recalculate();
}

if (full) {
    full.addEventListener("click", setFull);
}


// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.


                                //WHAT?

/********* calculate *********/
// when a calculation is needed, set the innerHTML of the calculated-cost element to the appropriate value

function recalculate() {
    total = days * rate;
    document.getElementById("calculated-cost").innerHTML = total
}

