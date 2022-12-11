Buckle up, here we go. 

To run: python3 manage.py runserver 

TABLE OF CONTENTS: 
PART I: Introduction / Background
PART II: How to Use 
PART III: How it Was Built 


PART I: Introduction / Background 

    DarmokTrack was conceived after I quit my job about a month ago and decided to dedicate myself to school full-time while I finally finish my degree. Within about thirty minutes of being unemployed, I realized that doing nothing but school would make me crazy, so I spun up an LLC to do some consulting on the side. Thus Darmok Consulting LLC was born. I quickly realized that without the service ticket software I used at my previous place of employment, I would need a reliable way to keep track of projects and the time spent on them, as well as an easy way to generate invoices for my consulting clients. Enter: DarmokTrack. 

    The application is built on a Django framework with some help from Python (and very minimal javascript) with a Bootstrap front end. My initial conception was almost entirely javascript-based, but as I went I realized that using javascript was hateful and it was much easier to do almost everything without it. 

PART II: How to Use

    DarmokTrack is (hopefully) pretty intuitive, but here is how to use it in a nutshell: 

    1) First things first, register for an account. I hope this goes without saying. 

    2) Once you've registered and logged in, you have a few different options: 
        a) My Projects: This is a view of all your active projects. Since you've just registered, there won't be much here yet! 
        
        b) New Project: Here is where you enter your first project. You can enter the name of your customer, the project name, how many hours you think it will take, and what the estimated budget is. 
        
        c) New Task: On this screen, you can add tasks to any of the Darmok Consulting projects (even if it is not one managed by you). In my experience, Project Managers love generating work for other teams, now is your chance! 
        
        d) Invoices: This is where you can get a list of all invoices for your projects. 

    3) Once you've created a project (step 2b) it's time to do stuff with it! Click "My Projects" from the navigation bar, and you'll be taken to a list of all of your open projects. From this screen you can click "Edit" to edit any of the initial project details, or Invoice to generate an invoice for the project. Most importantly, you can click the name of the project (formatted as "Customer - Project Name"), and this is where the magic happens! 

    4) After clicking into an individual project you have all sorts of options. To start, you see all the current information for this project. Just like on the project list, you can edit the original information or generate an invoice. If you keep scrolling you get: 

        a) Add Time to Project: very self-explanatory, this is where you keep track of time spent. You click the button to "Start Working" when you start, and it will automatically enter the current date and time. When you're done, just press "Stop Working" and it will enter your stop time. After that, click "Submit Time" and the elapsed time will be saved against the project! You can do this as many times as you want, it will keep adding the new elapsed time value to the existing total, so you don't lose track of any of your important billable time! :) 
        
        b) Add Expenses to Project: this is how you get reimbursed for any expenses incurred while working on the project. For example, if you have to pay for parking at the client site, you would just enter the date (with a convenient calendar pop-ou), how much parking cost, and a brief description, e.g. "parking meter." This expense will be added to the total invoice for the project. 
        
        c) Add Tasks to Project: Projects can have a lot of moving parts, and it's important to keep track of what needs to be done versus what has already happened. To add a task, just enter the description, choose who is responsible for executing it, and the due date (by default this is one week in the future). The task will show up at the top under the project information. From there, you can click the task name to update the description, owner, and to update the status (e.g. when you finish, you can change it from todo to complete). 

PART III: How it Was Built 

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
    - Same deal as the other stuff, there is a model and a form to fill out and a view and it displays stuff on the page. 

    INVOICE:
    - Generating the invoice on the screen was easy, I basically just copied what was making all the info display on the project screen minus the forms, and prettied it up with bootstrap
    - Getting the invoice to print to PDF was a different story. This is one of those things that sounds like it should be super easy but I had to try a few different methods to get it to work. 
