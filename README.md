# Django Task - Exception Middleware

## Tasks

### Django Middleware

- Create a Django middleware that checks whether the view raised an exception and creates a background task using Celery, which persists the exception on disk.
- The middleware should let the exception propagate to the other middleware.
- The exception info that should be stored are the exception type, the exception string (using str()), the exception representation (using repr()), the exception args and the traceback (as a string).

### API (Use Django Rest Framework for these)

- Create an API endpoint which raises an exception (any exception you want with any data).
- Create an API endpoint with which the user can view the exceptions that the middleware saved.

### Unit test
- Create tests for the middleware and the endpoint that returns the exceptions to the users

## Prerequisites
#### Python and pip
Make sure to install Python >= 3.0 with `pip` package manager.

#### Redis
Make sure that redis is installed on the box you're testing on. Redis should listen on:
| host | localhost |
|------|-----------|
| port | 6379      |

If you need to change this settings, edit `exercise/exercise/settings.py`, line 131 - `BROKER_URL` variable.

## Instructions
### pip
CD into `/excercise/`, ie. project root. Then, in your favorite console, issue following `pip` command to make sure proper package versions are installed. Note: it's advisable that you use virtualenvironment, so that you don't install python pip packages globaly.

`pip install -r requirements.txt`

After this, all the required dependencies will be satisfied.

### Celery
Open new terminal, or command prompt if on Windows. If you've created virtualenv in previous step, make sure that you activate it. Use following command to run celery:

`celery -A exercise worker --pool=solo -l info`

Note: Since Windows is no longer supported in Celery 4, we need to use single-pooling. More info can be found at: https://github.com/celery/celery/issues/4178

### Django
Switch back to previous terminal, the one you used with pip, and run django in development server:

`python manage.py runserver`

NOTE: by default, django will bind the 127.0.0.1 on port 8000 to the server.

### Requests
#### Make Exceptions
For the following commands, make sure you have `curl` installed, and added to PATH. There are 3 manually thrown exceptions in the code, and each of the following command corresponds to one of them. Feel free to run all three requests.

`curl -X POST http://127.0.0.1:8000/api/ -F e=object`
`curl -X POST http://127.0.0.1:8000/api/ -F e=field`
`curl -X POST http://127.0.0.1:8000/api/ -F e=result`

#### Get Exceptions
To get saved exceptions(assuming you did the previous step), issue the following command:

`curl -i -H "Accept: application/json" http://127.0.0.1:8000/api/`

or simply navigate to http://127.0.0.1:8000/api/ in your browser. 
