//Accessing data inside of nested data structures
//----------------------NESTED DATA STRUCTURES EXPERIMENT---------------------------------
const activities = { //<-- Level 1: Array
    savedActivities: [//<-- Level 2: List
        {//<-- Level 3: Array
            name: "To do this weekend",
            activities: [ //<-- Level 4: List
                "Cook one new recipe",
                "Go for a run",
                "Water plants"
            ],
            id: "1"
        },
        {
            name: "Fun fall activities",
            activities: [
                "Visit pumpkin patch",
                "Have a photo session of cat",
                "Write a note of appreciation to someone"
            ],
            id: "2"
        },
        {
            name: "Winter goals",
            activities: [
                "Go skiing",
                "Visit the beach",
                "Read War and Peace"
            ],
            id: "3"
        }

    ],
    completedActivities: [
        {
            activity: "Learn how to whistle with your fingers",
            id: "1"
        },
        {
            activity: "Create and follow a savings plan",
            id: "2"
        }

    ]

};

//Lets start by getting each "name" value out of the saved activities array.
let activityMap = activities.savedActivities.map(item => item.name);
// console.log(activityMap); // Returns all of the name values
// console.log(activityMap[0]); // Returns the name value at index 0 in 

//Lets try it with activities
let activityMap2 = activities.savedActivities.map(item => item.activities);
// console.log(activityMap2);
// console.log(activityMap2[0]);
console.log(activityMap2[0][0]);
