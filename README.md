[![Launch Live Demo] (https://shields.io)](https://trainings-database.onrender.com)

# Employee Training Record Tracker

## Project Overview

This is one of the projects that I developed during my time at the **Ford Motor Company**. The project helps administrators to manage and keep track of training records for both permanent employees and external contractors.

The application allows administrators to:
* Capture an employee's training session as soon as they complete the training.
* View an employee's training record (profile)

Department managers are able to:
* Approve or decline new sign ups to the system.

## Tech Stack and Hosting

**Backend:** Python (Django)  
**Database:** PostgreSQL  
**Frontend:** HTML & CSS  
**Application Hosting:** Render.com  
**Database Hosting:** Neon.tech

**Note:** Some content and system functionality may be changed due to company policy and data privacy restrictions. Website may take a few seconds to load due to server hibernation.

## How To Run Locally

1. **Clone the repository** 
   
   Make sure you're on a terminal like Git Bash or cmd.\
   git clone
   
3. **Create and activate a virtual environment** 
   
   Python -m venv env\
   source env/Scripts/activate
   
5. **Install dependencies** 
   
   pip install -r requirements.txt

7. **Environment setup** 
   
   Navigate to the .env file and change the database URL to point to your local PostgreSQL engine.\
   Navigate to the settings.py file and change the DEBUG variable to True.\
   Navigate to the ALLOWED_HOSTS list and remove everything to leave the list empty.
   
9. **Run the database migrations** 
    
    python manage.py migrate

11. **Run the project** 
    
    python manage.py runserver
   

**Note:** Some content and system functionality may be changed due to company policy and data privacy restrictions. Website may take a few seconds to load due to server hibernation.
