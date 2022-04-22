// In-Class: DOM Review

//This is needed to render everything on the page.
//Write this FIRST before anyother DOM's
document.addEventListener("DOMContentLoaded", function(){

    console.log("The Dom's Content is Loaded");//<-- This will output to the console on google chrome 

    //Gets the calculator's display
    const display = document.getElementById("display");
    // console.log(display); //<-- This will output to the console on google chrome 

    //Gets all the buttons on the page 
    const buttons = document.getElementsByTagName("button");
    // console.log(buttons); //<-- This will output to the console on google chrome 

    //NOTE: "buttons" is an object

    //Target the first button
    const buttonOne = buttons[0];
    // console.log(buttonOne); //<-- returnns the first button to the console

    let currentButton = null;
    for (let index=0; index<buttons.length; index++){
        const currentButton = buttons[index];
        currentButton.addEventListener(`click`, function(event){
            
            //If statement targets all the buttons clicked
            if (event.target.id){
                //Responds to all buttons clicked
                display.innerText = display.innerText + event.target.id;
            }

            //If statement targets makes sure that there are no duplicates




        });
   




    }







    }
); 




