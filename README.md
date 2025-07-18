# Project Task Manager

## Site Overview
The Project Task Manager is a full-stack web application designed to help users effectively manage their business workflow. Users can create and manage multiple projects, add and edit associated tasks, and maintain an organised dashboard of their ongoing work. The app supports role-based access and offers user authentication to ensure data privacy and security.
________________________________________
## Table of Contents
1. Site Overview
2. User Stories
3. Features
4. Tech Stack
5. Wireframes
6. Database Schema
7. Future Enhancements
8. Testing
9. Deployment
________________________________________
## User Stories
### As a Registered User, I can:
-   Register an account and log in securely so I can manage and access my personalised project and task dashboard.
-	Create new projects with a title and description to keep track of my new projects and keep notes on their content and goals.
-	View a list of all my projects so I can monitor progress across different streams of work.
-	Edit or delete existing projects in case project requirements change or a project is no longer relevant.
-	Create tasks under specific projects to break down my project into smaller actionable steps.
-	Assign due dates and mark task completion to track deadlines and ensure timely delivery.
-	Edit or delete individual tasks to reflect any changes in the task scope or status.
-	View tasks grouped by project for better workflow management and improved visibility.
-	Log out of my account securely to ensure my data remains private and protected.
### As an Unregistered User, I can:
-	Visit the home page to understand the purpose of the platform.
-	Register for a new account to start creating and managing my projects and tasks.

### As a Site Admin, I can:
-	Access the Django admin panel to manage users, projects, and tasks.
-	Monitor all registered users and their project/task data for quality control and platform integrity.
-	Remove inappropriate or duplicate content to maintain a clean and professional environment.
-	Add featured content or announcements to improve user engagement and communication.


________________________________________
## Features

- Landing page, the landing page is the first page you are greted with when you load the site, it displays a welcome message. This page dispalys a regsiter and login button which can be selected depenending on if the user has already made an account both buttons take you to the corresponding pages. 

<p align="center">
 <img src="assets/images/features Landing page.png" alt="landing page"/>
</p>

- Registration page, this page is for users who dont have an account and would like to register, it conatins text boxes for the username, password and password confirmation. It also has instruction for the parameteres of the username and password and validation to confirm the passwords match and both things meet the set criteria before the user can register. once the boces are filled correctly the user can click the register button and will be taken to the login page.

<p align="center">
 <img src="assets/images/features registration page.png" alt="Registration page"/>
</p>

- Login page, this page is simple with a title saying login anf two textboxes for the user to enter their credentials they made when they registered. there is a login button at the bottom that will log them in when correct credentials are entered. 

<p align="center">
 <img src="assets/images/features login page.png" alt="login page"/>
</p>

- Your projects page, this page shows once a user is logged in, if the user has created projects they will show if not it will show they have no projects. On this page they can edit or delete projects if they have them or add new projects if they dont have any made. they can also click on previously made projects to view them and edit them. this page has 4 buttons, one to log out, one to add new a projects and then two buttosn for editing and deleting previously made projects. 

<p align="center">
 <img src="assets/images/features your projects.png" alt="your projects page"/>
</p>

- Add new project page, the add new project page has a text box to enter the project name and description, once this is done you can create the project or you can go back to the previous page or you can click add new project to refresh the page. 

<p align="center">
 <img src="assets/images/features add new project.png" alt="add new projectt page"/>
</p>

- Edit project page, this page allows you to edit previously created projects. Once you have done that you can press the save chnages button.

<p align="center">
 <img src="assets/images/features edit project.png" alt="edit project page"/>
</p>

- Delete project page, this page allows you to delet previously creted projects. if you want to delete you can confirm by clicking yes delete button or cancel with the cancel button.

<p align="center">
 <img src="assets/images/features delete project.png" alt="delete project page"/>
</p>

- Add task page, this page allows you to add task to your project, it contains text fields for:title, description, drop down for which prject it is assigned to, drop down for the status and due date. once that it completed you can click the create task button.

<p align="center">
 <img src="assets/images/features add task.png" alt="add task page"/>
</p>

-	User registration and authentication (login/logout)
-	Role-based access control
-	Project CRUD (Create, Read, Update, Delete)
-	Task CRUD within each project
-	Responsive navigation bar
-	Bootstrap integration for a mobile-friendly interface
-	Feedback messages on key actions (e.g. task added, project deleted)
________________________________________
## Tech Stack
### Languages & Frameworks
-	Python
-	Django
-	HTML5
-	CSS3
-	JavaScript
### Libraries & Packages
-	Bootstrap 5
-	dj-database-url
-	gunicorn
-	psycopg2-binary
-	Whitenoise
-	Django Allauth
### Tools & Platforms
-	Visual Studio Code
-	Git & GitHub
-	Heroku (for deployment)
-	PostgreSQL (for production database)
________________________________________
## Wireframes
Wireframes were created during the planning phase to visualise the user interface and page layout. These include: 
- Home Page 
<p align="center">
 <img src="assets/images/wireframe homepage.png" alt="wireframe of home page"/>
</p>

- Project/task List Page 
<p align="center">
 <img src="assets/images/wireframe Projects-task list.png" alt="wireframe of project list page"/>
</p>

- Project Create Page 
<p align="center">
 <img src="assets/images/wireframe project create.png" alt="wireframe of project create page"/>
</p>

- Task Create Page 
<p align="center">
 <img src="assets/images/wireframe create task.png" alt="wireframe of create task page"/>
</p>

- Login/Register Pages
<p align="center">
 <img src="assets/images/wireframe login.png" alt="wireframe of login page"/>
 <img src="assets/images/wireframe register.png" alt="wireframe of register page"/>
</p>
I created draft mockups of the wireframes on powerpoint and then inserted screenshots of these with an explanation of what my project was to Chatgpt to render the images you see here. i wanted to keep my design simplistic and professional as it is mainly intended for office use and as an organisational tool. These wirefraames are very basic and in future projects i would use better software to create more detaiiled wireframes.
________________________________________

## Database diagram

<p align="center">
 <img src="assets/images/Database diagram.png" alt="Database Diagram"/>
</p>

I created a dtabase digram draft on powerpoint and uploded this to ChatGPT with my models.py file to crete the following dtatabse digram showing the flow and realtion of the functions and corresponding databse on the website.


________________________________________
## Future Enhancements
In the future the developments i would make to improve this site are as follows:
-	Implement user roles (e.g. admin, manager, team member)
-	Task assignment to multiple users
-	Project categories/tags for filtering
-	Calendar view of tasks and deadlines
-	Notifications for task due dates
-	Export project/task data to CSV or PDF

Other improvements can be made in later iterations.
_______________________________________
## Testing
Manual testing was carried out across different devices and browsers to ensure: Responsive design and consistent layout, successful creation, editing, and deletion of projects and tasks, correct redirection and error handling, validation on forms to prevent blank or incorrect submissions and login/logout functionality behaves as expected.

Django’s built-in testing tools were also used to confirm: model integrity, view rendering and URL routing.

### python manage.py test results:
<p align="center">
 <img src="assets/images/python manage.py test.png" alt="image of test results from django test using test.py"/>
</p>
Test shows no issues with python/django tested. check passed.

### Flake8 test result to ensure compliance with pep8:
<p align="center">
 <img src="assets/images/flake8 test.png" alt="flake8 test results"/>
</p>
The results show some minor issues with ling length and spaces these issues do not impact the code and would cause issues wfi they were ammended. therefore, they will be left as they are.

### W3C CSS validation:
<p align="center">
 <img src="assets/images/w3c test result.png" alt="W3C test results"/>
</p>
I tested my website with W3C and it found no errors.

### lighthouse test results:
<p align="center">
 <img src="assets/images/Landing page test.png" alt="landing page test results"/>
 <img src="assets/images/add new project test.png" alt="add new project page test results"/>
 <img src="assets/images/your projects test.png" alt="your projects page test results"/>
</p>
I tested all of my pages using lighthouse with scored varying but never dropped below 96 overall.

After both manual and automated testing i did not find any issues that would have a measurable impact on the website.
Issues i did come acroos when testing was an error with the server when deploying this was fixed through trouble shooting in various ways, i also tested all the features on the website to ensure functionality, i found some issues with adding and editing task which led to them not being stored in the project which was also fixed.
________________________________________
## Deployment
### Platform
-	Deployed on Heroku using the Heroku CLI
Steps Taken:
1.	Created Procfile, requirements.txt, and runtime.txt
2.	Configured ALLOWED_HOSTS in settings.py
3.	Set up Heroku PostgreSQL and added environment variables:
-	DATABASE_URL
-	SECRET_KEY
-	DISABLE_COLLECTSTATIC
-	DJANGO_DEBUG
4.	Ran migrations and created a superuser using Heroku CLI
5.	Used collectstatic for static files
6.	Pushed final version to GitHub and Heroku
### Issues Encountered:
-	Initial 400 Bad Request due to missing Heroku domain in ALLOWED_HOSTS
-	Database misconfiguration due to unset DATABASE_URL
-	Static files not loading until Whitenoise and collectstatic were correctly configured
These issues were resolved during deployment and are now fully functional.

## User Authentication
all the pages on the site reuire user authentication this means that they cannot view any snesitive information without being logged in. this avoids users acessing snesitive information and chnaging content for other users.

## Media
Media was only used for the readme, all files were screenshots taken from the website and then saved and uploaded locally to vscode.

## Credits

1. Design & UI Tools
Bootstrap 5 – for layout, components, and responsiveness
Credit: https://getbootstrap.com

2. Wireframe and ERD Creation
Created wireframes and database diagrams using AI: Wireframes and database schema generated using OpenAI tools.

3. Packages & Libraries:

- dj-database-url
- gunicorn
- whitenoise
- psycopg2-binary
- Django Allauth

4. Deployment Platform
-Heroku
App deployed using Heroku: https://heroku.com

5. Acknowledgements:
- Code institute LMS and learning materials 
- general pnline forums for help with trouble shooting
- openAi for help with troubleshooting and bug fixes
________________________________________
Final Deployment: https://project-task-manager-cffc460251b6.herokuapp.com/
GitHub Repository: https://github.com/Zee-5p/project-task-manager.git
