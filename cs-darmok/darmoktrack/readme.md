Buckle up, here we go. 

DarmokTrack was conceived after I quit my job about a month ago and decided to dedicate myself to school full-time while I finally finish my degree. Within about thirty minutes of being unemployed, I realized that doing nothing but school would make me crazy, so I spun up an LLC to do some consulting on the side. Thus Darmok Consulting LLC was born. I quickly realized that without the service ticket software I used at my previous place of employment, I would need a reliable way to keep track of projects and the time spent on them, as well as an easy way to generate invoices for my consulting clients. Enter: DarmokTrack. 

The application is built on a Django framework with some help from Python (and very minimal javascript) with a Bootstrap front end. My initial conception was almost entirely javascript-based, but as I went I realized that using javascript was hateful and it was much easier to do almost everything without it. 

The main parts of DarmokTrack are as follows: 

REGISTRATION:
- The registration, log in, and log out functions were all borrowed from earlier CS50 assignments. Users are able to register for an account and then log in and log out of that account. The standard User function is used in Django because it works spectacularly well.  

MY PROJECTS:
- This screen just displays a list of all active projects associated with the user. It uses the Django views to filter out projects that do *not* belong to the user, so they can only see the ones that they've created. The Project model in Django has all the info associated with it that is required, including: 
    - The Project Manager (this is how the application knows which user can see what projects) 
    - Project details including name, start date, customer, budgeted hours, and budgeted dollars
    - Whether the project is active or inactive 
- The projects are ordered in reverse chronilogical order from their start date, because it seemed logical to put the newest ones on top and the oldest on the bottom
- I also had to calculate the elapsed time for the project in the Project Model. This took a LOT of trial and error, and I am reasonably certain I invented some new colorful metaphors in the process of trying to get this to work. Originally I had it in the TimeModel model, but it wound up needing to be associated with the Project model to affiliate with the Project, so voila. 

NEW PROJECT:
- To create a new project was just another Django form. The Model Form is one of my favorite things about Django because it makes form-ing so simple that even a complete novice (such as myself) is able to do it without too much trouble. This was actually the first part of the application that I put together, because I knew that it would be the easiest part, and it was!
- This is the first time I've used crispy forms, after seeing them in documentation over and over. I like how nicely formatted the form is, and I'll likely crisp up future forms as a result. 

TRACK:
- Originally I had conceived of time tracking as being wholly in Javascript. I actually got a live timer working, where the user could click to start and stop and the timer would run. Unfortunately, getting that to actually write into the models proved beyond my meager abilities. As a workaround, I looked at the service ticketing application I used in my last job. It had a little clock, and the user would click the clock and it would fill in the start time, then they would click it again to fill in the end time, they type their notes and hit save. I used javascript so that the user can just click the button and it will enter the current time instead of them having to do it themselves. This way it can automatically format in the ISO format so it doesn't keep throwing "invalid response" errors, which it did at first. That was vexing to a level I can not even articulate, and it took a lot of googling to figure out that it wasn't a problem with my form but just that the datetime has to be entered in a very specific way. 

EXPENSES: 
- 

INVOICE:

