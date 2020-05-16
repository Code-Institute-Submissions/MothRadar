# Code Institute Milestone Project 4 - Django bug tracker app

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)



## Deployment

**The deployed app can be found here: [MothRadar](https://mothradar-ba79.herokuapp.com/)**

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use `pip install` to install `dj-database-url`, `whitenoise` and `gunicorn` (psycopg2 has already been installed).
4. Run `pip freeze --local > requirements.txt` to update the requirements file.
5. From Heroku App Config Vars (Settings tab), copy the DATABASE_URL.    
In env.py, add the `DATABASE_URL`, a `DEVELOPMENT` environment variable with the value of `"1"`, and a `LOCALHOST`variable`.
6. In settings.py, import the `DEVELOPMENT` variable and set `DEBUG` dependent on the value of the `DEVELOPMENT` variable:
```python
if os.environ.get("DEVELOPMENT"):
    development = True
else:
    development = False
DEBUG = development
```
7. In settings.py, import dj_database_url.
Under `DATABASES`, comment out the Sqlite database and add the Postgres database:
```python
DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
```

8. Run `python manage.py makemigrations` and then `python manage.py migrate`.

9. In settings.py, under `DATABASES`, uncomment the Sqlite database and set the database selection (Sqlite and Postgres) depending on the `DEVELOPMENT` variable:
```python
if os.environ.get("DATABASE_URL"):
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
10. In settings.py, under `MIDDLEWARE`, add `whitenoise.middleware.WhiteNoiseMiddleware`.   
At the bottom of the file, add:
```python
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

11. In the root of the project workspace, create a Procfile (capital P!) with the following content:
`web: gunicorn mothradar.wsgi:application`
Save the file.

12. Still in the root create a folder named "static".

13. From env.py, copy the following environment variables and their values (without quotes!) into Heroku App Config Vars:
```python
SECRET_KEY
EMAIL_ADDRESS
EMAIL_PASSWORD
STRIPE_PUBLISHABLE
STRIPE_SECRET
```
Add a `DISABLE_COLLECTSTATIC` Config Var and set its value to 1.

14. In settings.py, get the `LOCALHOST` environment variable as `localhost`.   
Under `ALLOWED_HOSTS`, add `mothradar-ba79.herokuapp.com` and `localhost`.

15. In Terminal, `run python manage.py collectstatic`.

16. Commit and push all changes to GitHub master. 

17. In Heroku App DashBoard, under the Deploy tab, select GitHub as Deplyoment method. In the searchbox, type the name of the GitHub repo (MothRadar) and click "Connect".     
Under Manual deploy, make sure that the selected branch is **master**, and click Deploy Branch.

18. The app is now deployed on Heroku.



## Acknowledgements

- Favicon image was obtained from [publicdomainvectors.org](https://publicdomainvectors.org/).
- [convertio.co](https://convertio.co/) was used to convert favicon image from SVG to PNG.
- [favicon.io](https://favicon.io/) was used to generate favicon.


## Code validation:

### HTML 

Validated using [W3c Markup Validation Service](https://validator.w3.org/).
Issues found:
1. Register form -  "Element **ul** not allowed as child of element **small** in this context."
2. Password Reset form -  "Element **ul** not allowed as child of element **small** in this context."
3. Password Change form -  "Element **ul** not allowed as child of element **small** in this context."
These issues are related to the way Crispy Forms handles the Registration Form.

### CSS

Validated using [W3c CSS Validation Service](http://jigsaw.w3.org/css-validator/).   
No issues were found.

### JS

Validated using [JSHint](https://jshint.com/).   
No issues were found.

