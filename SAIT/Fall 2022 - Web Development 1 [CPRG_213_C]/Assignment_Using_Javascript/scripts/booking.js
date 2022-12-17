/********* create variables *********/
// useful variables might be: the cost per day, the number of days selected, and elements on the screen that will be clicked or will need to be modified. 
// Do any of these variables need to be initialized when the page is loaded? 
// When do they need to be reset or updated?

var CPD; //Cost Per Day
var NODS; //Number of Days Selected
var PRATE; //Price Rate
var T; //Total Cost
var C_Button = document.getElementById("Clear-Button") //To Reset Button Contents

//Variables for Weekdays 
var MON =  document.getElementById("Monday"); 
var TUE =  document.getElementById("Tuesday");
var WED =  document.getElementById("Wednesday");
var THUR =  document.getElementById("Thursday");
var FRI =  document.getElementById("Friday");

//Variables for Amount of the Day
var FULL = document.getElementById("Full");
var HALF = document.getElementById("Half");

/********* colour change days of week *********/
// when the day buttons are clicked, we will apply the "clicked" class to that element, and update any other relevant variables. Then, we can recalculate the total cost.
// added challenge: don't update the dayCounter if the same day is clicked more than once. hint: .classList.contains() might be helpful here!

if (MON) {
    MON.addEventListener("Click", Update.bind(null, MON));
}

if (TUE) {
    TUE.addEventListener("Click", Update.bind(null, TUE));
}

if (WED) {
    WED.addEventListener("Click", Update.bind(null, WED));
}

if (THUR) {
    THUR.addEventListener("Click", Update.bind(null, THUR));
}

if (FRI) {
    FRI.addEventListener("Click", Update.bind(null, FRI));
}

function Update(DBUTT) {
    DBUTT.classList.add("Clicked");
    CPD += 1;
    RECALCULATE();
}

/********* clear days *********/
// when the clear-button is clicked, the "clicked" class is removed from all days, any other relevant variables are reset, and the calculated cost is set to 0.


function CBUTT() {
    MON.classList.remove("Clicked");
    TUE.classList.remove("Clicked");
    WED.classList.remove("Clicked");
    THUR.classList.remove("Clicked");
    FRI.classList.remove("Clicked");
    CPD = 0;
    T = 0;
    SETFULL();
}

if (C_Button) {
    C_Button.addEventListener("Click", CBUTT);
}



/********* change rate *********/
// when the half-day button is clicked, set the daily rate to $20, add the "clicked" class to the "half" element, remove it from the "full" element, and recalculate the total cost.

function SETHALF() {
    PRATE = 20;
    HALF.classList.add("Clicked");
    FULL.classList.remove("Clicked");
    recalculate();
}

if (HALF) {
    HALF.addEventListener("Click", SETHALF);
}

// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.

function SETFULL() {
    PRATE = 35;
    FULL.classList.add("Clicked");
    HALF.classList.remove("Clicked");
    RECALCULATE();
}

if (FULL) {
    FULL.addEventListener("Click", SETFULL);
}


// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.


                                //WHAT?

/********* calculate *********/
// when a calculation is needed, set the innerHTML of the calculated-cost element to the appropriate value

function RECALCULATE() {
    T = CPD * PRATE;
    T = document.getElementById("Calculated-Cost").innerHTML
}

