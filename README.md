# QuickCheck Python Test 

*Summary of Task
1.  Fetch data from the TOP STORIES ENDPOINT every 5 minutes(scheduled Job) and sync it to the database. I used 3 endpoints since the Job, Ask and Story Endpoints returns different json object with different key/value pairs.

2. Implement a view to list all top stories, and allow filtering by item, search filtering by text, and enable pagination.

3. Expose the data in DB as API with a GET and POST method
    a) GET METHOD: List all items with filtering enabled
    b) POST METHOD: Add a new item that is not present in DB(items from  hacker news API)

4. Allow PUT and DELETE methods(But not for data fetched from hacker news API)


## Folder Structure
* HNAPIS: 
        This is the App that holds project API Endpoints 

* HNAPP: 
        This module handles application logic for the project. API calls are made from the tasks.py file.

* HNPROJECT: 
        This is the applications project

* JOBS: 
        This folders was used for testing the API, background scheduler was used for the scheduled API calls(disabled)
 
* TEMPLATES: 
        The project frontend views are kept here;

## Requirements
* Python 
* RabbitMQ or Redis as Message Broker(RabbitMQ was used)
* Install all packages in the requirements.txt file

## How to run the application
* clone this repository and cd inside your project root directory and create a virtual environment. 
* Run - `python -m venv ./venv` This will install your virtual environment, all dependencies will live here.
* Activate the virtual environment by using the command - `. venv/scripts/activate` 
* Install all requirements by using `pip install -r requirements.txt`
* Run `py manage.py makemigrations`.
* Run `py manage.py migrate`.
* Start development server by running the command `py manage.py runserver` 
* Type into your browser url the following command `localhost:8000` and the application index page will be up.

## Login admin user/password:
* username: hackernews
  password: hackernews123

## Start Scheduled Task:
    Go to project settings file. On line 154 of `CELERY_BEAT_SCHEDULE`
    uncomment out the code and apply appropriate time as desired

* ## Start Message Brokers: 
  
  - start celery worker on windows
        celery -A hnproject worker -l info --pool=solo

  - start celerybeat worker on windows
        celery -A hnproject beat -l INFO
                                                
**N.B:-** If any issue is encountered during setting up this application, kindly email me `Prosperibe12@gmail.com`.
