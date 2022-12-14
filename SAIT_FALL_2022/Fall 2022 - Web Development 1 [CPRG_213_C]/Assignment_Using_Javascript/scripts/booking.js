/********* create variables *********/
// useful variables might be: the cost per day, the number of days selected, and elements on the screen that will be clicked or will need to be modified. 
// Do any of these variables need to be initialized when the page is loaded? 
// When do they need to be reset or updated?

var NOD = 0; //Cost Per Day
var PRATE = 35; //Price Rate
var T; //Total Cost
var C_Button = document.getElementById("clear-button"); //To Reset Button Contents

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

function Update(DBUTT) //Day Button

{ 
    console.log(NOD);

    if (DBUTT.classList.contains("clicked"))
    
    {

        NOD = NOD;

    }

    else
    
    {

        NOD += 1;
        DBUTT.classList.add("clicked");
    
    }

    RECALCULATE();
}

if (MON) 

{

    MON.addEventListener("click", Update.bind(null, MON));

}

if (TUE) 

{

    TUE.addEventListener("click", Update.bind(null, TUE));

}

if (WED) 

{

    WED.addEventListener("click", Update.bind(null, WED));

}

if (THUR) 

{

    THUR.addEventListener("click", Update.bind(null, THUR));

}

if (FRI) 

{

    FRI.addEventListener("click", Update.bind(null, FRI));

}

/********* clear days *********/
// when the clear-button is clicked, the "clicked" class is removed from all days, any other relevant variables are reset, and the calculated cost is set to 0.


function CBUTT() //Cancel Button

{ 
    MON.classList.remove("clicked");
    TUE.classList.remove("clicked");
    WED.classList.remove("clicked");
    THUR.classList.remove("clicked");
    FRI.classList.remove("clicked");
    NOD = 0;
    T = 0;
    SETFULL();

}

if (C_Button) 

{

    C_Button.addEventListener("click", CBUTT);

}

/********* change rate *********/
// when the half-day button is clicked, set the daily rate to $20, add the "clicked" class to the "half" element, remove it from the "full" element, and recalculate the total cost.

function SETHALF() 

{

    PRATE = 20;
    HALF.classList.add("clicked");
    FULL.classList.remove("clicked");
    RECALCULATE();

}

if (HALF) 

{

    HALF.addEventListener("click", SETHALF);

}

// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.

function SETFULL() 

{

    PRATE = 35;
    FULL.classList.add("clicked");
    HALF.classList.remove("clicked");
    RECALCULATE();

}

if (FULL) 

{

    FULL.addEventListener("click", SETFULL);

}

// when the full-day button is clicked, the daily rate is set back to $35, the clicked class is added to "full" and removed from "half", and the total cost is recalculated.


                                //WHAT?

/********* CALCULATE *********/
// when a calculation is needed, set the innerHTML of the calculated-cost element to the appropriate value

function RECALCULATE() 

{

    T = NOD * PRATE;
    document.getElementById("calculated-cost").innerHTML = T;
    
}