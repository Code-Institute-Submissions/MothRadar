# MothRadar

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)


MothRadar is a ticket tracker app for a fictional application called UnicornAttractor. MothRadar enables the users of the UnicornAttractor to raise tickets on issues encountered during the app use, to browse through existing tickets, and to comment on them. It also provides the users with the ability to upvote existing tickets, thus helping the UnicornAttractor app owner to prioritise fixes among existing bugs.

_"MothRadar never loses track of any bug that enters its scope."_

## UX

MothRadar is intended primarily for the users of the UnicornAttractor app. It also aims to facilitate the owner's maintenance work on the app by providing user feedback in the form of tickets, comments and upvotes.

Visitors (unregistered users and users not logged-in) have only the option to browse, search and filter existing tickets and view individual ticket details (read-only access).

Registered and logged-in users have access to the full set of features of the MothRadar app: new ticket creation, commenting on existing tickets, and upvoting tickets. 

Tickets can be raised as one of two types: **Bug** (for UnicornAttractor app issues) or **Feature** (for suggestions on app improvement). The structure and handling of either ticket type in MothRadar is identical, with the exception of the Upvote feature which is free for Bug tickets but requires payment for Feature tickets.   

### User Stories

Based on the above general requirements, the following user stories have been identified:

As a user:
1. I want to be provided with some general information on the MothRadar app's available features and how to use them.
2. I want to be able to create a new ticket.
3. I want to be able to edit/amend a ticket that I have created.
4. I want to be able to browse existing tickets.
5. I want to be able to search existing tickets by keyword(s) to narrow my browsing scope.
6. I want to be able to view the most upvoted tickets.
7. I want to be able to filter my tickets only.
8. I want to be able to filter by Bugs only or Features only.
9. I want to be able to view all details of a selected ticket, including date created, author, upvotes count, and existing comments on the ticket.
10. I want to be able to comment on an existing ticket in order to provide more details if I have them.
11. I want to be able to edit my comment(s).
12. I want to be able to delete my comment(s).
13. I want to be able to upvote a ticket I find relevant for me, so I can get it fixed sooner.
14. I want to be able to view my account details.
15. I want to be able to edit my account details.
16. I want to be able to change my password.
17. I want to be able to log out so I can protect my account when I am finished working with the app.
18. I want to be able to reset my password via email if I forget it.

As app owner:   
1. (19) I want to have a user login functionality.    
2. (20) I want only logged-in users to be able to make changes to the existing ticket data (ticket details, comments and upvotes).
3. (21) I want a logged-in user to be able to edit ticket details only for tickets they have created, and only if the ticket is still in its initial status.
4. (22) I want not logged-in users to be able to browse-only the site.
5. (23) I want to provide a visitor with the option to register and create a user account.
6. (24) I want to have a payment process for logged-in users upvoting Feature tickets.




### UI structure

#### Essential elements

_Due to time constraints, it has been decided that, with regards to comments, in this version of the app only creation of comments will be enabled. Editing and deleting of existing comments (by their creator only) - **user stories 11 and 12 - will need to be implemented in a future version.**_ 

The following UI elements are essential for the implementation of the user stories:

- navigation bar/menu,
- landing page,
- ticket creation form,
- ticket search form,
- ticket filters/views:
    - most upvoted,
    - created by user,
    - Bugs only,
    - Features only,
- new comment form,
- upvote button and counter,
- logout button,
- user login form,
- user registration form,
- payment form.

The full stack of the app is built using the [Django](https://www.djangoproject.com/) framework.

Most of the needed forms are obtained either directly from Django default forms (User) or by defining Model forms (Ticket and Upvote) and rely on Django form validation. [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) are used for rendering of all Django-based forms.

The two exceptions to this are: 
- the Ticket Search form, which uses a GET method and therefore does not require validation, and 
- the comments "form", which uses JavaScript processing (including an Ajax call to backend) and is therefore not defined as an HTML form element but just as an HTML text area with a button to trigger the JavaScript script.


#### Visual layout

[Bootstrap](https://getbootstrap.com/) styling has been used as much as possible to assure full responsivity of the site. 

A top-fixed Bootstrap navbar with the essential links is present at all times. At screen sizes below 992px this is reduced to just the Logo and the "burger icon" which opens a "sidenav" with the links.
On screen sizes below 992px all content is displayed in single-column layout (screen-wide), while on large screens (992px and above) it is dependent on the actual page displayed.
Four [wireframe.cc](https://wireframe.cc/) wireframes (for desktop-size display) were produced during the prototyping phase of the project:

- [Home/Landing page](https://wireframe.cc/eGJAA4)
- [All Tickets view](https://wireframe.cc/3aDo54)
- [Ticket detail view](https://wireframe.cc/WFyuKF)
- [New ticket form](https://wireframe.cc/1KlXoR)

The only major departures from the initial design is in that the sidebar has been placed to the left of the main content (as opposed to the right in the wireframes) and that it has been removed on detail views as not needed.   
Also, the "by status" filter has been replaced by a "my tickets" filter.

#### Font and colour scheme

The "Open Sans" font from [Google Fonts](https://fonts.google.com/) was chosen for its professional appearance and readability. 

The colour scheme was chosen to mimic the "dark mode" settings of Windows, IDEs, Stack Overflow, Slack etc.    
Thus the basic background colour is a very dark (near-black) grey (#222121) with lighter or darker grey elements on top of it, whereas the main font colour is a very light grey (#b9b7b7) - pure white and off-white have not been used in order to avoid too strong a contrast.  
The only elements departing from this general scheme are buttons and badges (styled with Bootstrap default colour classes), alerts (default Bootstrap colour classes with occasional custom adjustments), links/anchors (default blue colour) and ticket type and status tags (custom colours). These details were chosen in order to add clear highlight to elements that point to a certain functionality, or to subtly highlight specific ticket data.


## Features

### Existing features

#### Navbar
The navbar is implemented as a Bootstrap top-fixed navbar with responsive layout (breakpoint 992px). The contents (links) in the navbar change dynamically depending on whether the user is logged in or not.

#### Landing page
The landing page is designed in the form of interactive cards which, when clicked, expand to reveal the details of certain features of the application.

#### Ticket list view
The default ticket list view displays the list of all tickets in the database sorted by date and time created (newest first).

#### Ticket list view filters/sorting
Four sort/filter options are available to all users: sort by most recent (default view), sort by most upvoted, filter Bug tickets only, and filter Feature tickets only.    
For logged-in users, a third filter is available to display only the tickets created by that user, the total number of those tickets being indicated in the sidebar.

The current selected view/filter is clearly indicated by the UI by colour-highlighting the corresponding view's link/button in the sidebar.

Pagination (5 tickets per page) is implemented in all list views.

#### Ticket list search
The search function is implemented as a simple search box with a button to trigger the search. 
The search is performed on top of any current view filters, so if e.g. the user has selected the "Features only" filter, the search will be performed among Feature tickets only.    

_Note: the current search functionality uses a simple `__icontains` on the Ticket model's `description` field. The plan is to implement a more complex search algorithm, and include both the `title` and the `description` fields, in a future version of the app._  

#### Ticket detail view
The ticket detail view provides any user with all details of the ticket (author, creation date, title, description, ticket type and ticket status), plus the upvotes count and the complete list of comments for the ticket.   
For logged-in users, this is expanded by:
- a button to upvote the ticket (if not already upvoted),
- a button to edit the ticket (if raised by the current user and if in "OPENED" i.e. initial status),
- a text area and a button to post comments.

#### Upvoting system

Ticket upvoting is login-dependent. Any ticket can be upvoted only once by an individual user.    

##### Bug ticket upvoting 
Bug ticket upvoting is free of charge.   
The status of the upvote button provides clear feedback on the availability of the upvote function for the current user (greyed out if the ticket is already upvoted by the user, and completely absent if the user is not logged in).   
A click on the available Upvote button provides the user with success feedback, greys out the button, and updates the upvote count.
##### Feature ticket upvoting
The UI for the initiation of Ticket upvoting is near-identical to the one described above, with two differences:
- a lock icon is displayed on the Upvote button in Feature tickets, to indicate a reserved feature, and
- click on the available Upvote button triggers a confirmation modal which informs the user that it is a paid service (including the price) and provides the user with the option to cancel the action or to continue.

Confirmation of the modal redirects the user to a Stripe Card Payment processing form. Only credit card details (card number, CVV, expiry month and expiry year) are required to complete payment, the user is asked for no personal information.

The user is informed about the payment status on every step of the process, either by an error text next to the payment button (in case of invalid CVV or expiry date/month) or by a closable Bootstrap alert at the top of the screen. 

#### User handling
User handling relies completely on Django authorisation and forms to create and update user data and to authorise users. Thus the user has the option to register, log in, log out, edit password, edit profile data, and reset password via email.  


#### Defensive design

Defensive design principles have been implemented wherever possible, namely by restricting the ability to add to the database (ticket creation, ticket updating, adding of comments, upvoting) to logged-in users only and by restricting the edit possibilities only to the data "owned" (authored) by the current logged-in user.   
 Wherever possible, the restrictions have been implemented both at the frontend (absence of access to buttons/views) and at the backend (login_required view decoration, filtering querysets by author).

### Features left to implement

1. Add a better search algorithm (ability to search by complex phrases, as well as to search on both ticket title and description).

2. For the logged-in user, add the ability to edit and delete own comments.

3. Add additional ticket statuses (e.g. "Analysed" - to indicate that the ticket has been attended to i.e. it is no longer in initial state - and "Closed", to indicate that either the fix has been fully validated or that a ticket has been resolved in some other way).

4. Add an algorithm to prevent the user from accidentally creating a duplicated ticket by going back to a previously created ticket's form (time constraints prevented this from being implemented in the current version).


## Database structure

On top of the Django User model, which has not been modified for this project, three more models have been created:

1. **Ticket** - with User as Foreign Key (`author`).

    <table><tr><th>id</th><th>title</th><th>description</th><th>ticket_type</th><th>status</th><th>author_id</th><th>date_created</th><tr><tr><td>2</td><td>Some issue 1</td><td>Some description of issue 1 edited</td><td>FEATURE</td><td>SOLVED</td><td>3</td><td>2020-05-02</td></tr><tr><td>4</td><td>Some issue 2</td><td>Description of Issue 2 in a few words...</td><td>BUG</td><td>INPROG</td><td>3</td><td>2020-05-02</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

2. **Comment** - with User and Ticket as Foreign Keys (`author` and `rel_ticket`).

    <table><tr><th>id</th><th>text</th><th>created</th><th>rel_ticket_id</th><th>author_id</th><tr><tr><td>1</td><td>Here is my very fist comment to a ticket.</td><td>2020-05-04 11:47:20.171831</td><td>2</td><td>1</td></tr><tr><td>2</td><td>One more comment to this issue</td><td>2020-05-04 11:47:38.591623</td><td>2</td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>


3. **Upvote** - with User and Ticket as Foreign Keys (`upvoter` and `ticket`).

    <table><tr><th>id</th><th>ticket_id</th><th>upvoter_id</th><tr><tr><td>46</td><td>23</td><td>1</td></tr><tr><td>47</td><td>21</td><td>1</td></tr><tr><td></td><td></td><td></td></tr></table>


All Foreign Keys have been set with `on_delete=models.CASCADE`.

Each of the four models is handled by a separate app - `users`, `tickets`, `comments` and `upvotes`.





## Deployment

**The deployed app can be found here: [MothRadar](https://mothradar-ba79.herokuapp.com/)**

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use `pip install` to install `dj-database-url`, `whitenoise` and `gunicorn` (psycopg2 has already been installed).
4. Run `pip freeze --local > requirements.txt` to update the requirements file.
5. From Heroku App Config Vars (Settings tab), copy the DATABASE_URL.    
In env.py, add the `DATABASE_URL`, a `DEVELOPMENT` environment variable with the value of `"1"`, and a `LOCALHOST` variable`.
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

9. In settings.py, under `DATABASES`, uncomment the Sqlite database and set the database selection (Sqlite and Postgres) depending on the `DATABASE_URL` variable:
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

12. Still in the root, create a folder named "static".

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

17. In Heroku App DashBoard, under the Deploy tab, select GitHub as Deployment method. In the search box, type the name of the GitHub repo (MothRadar) and click "Connect".     
Under Manual deploy, make sure that the selected branch is **master**, and click Deploy Branch.

18. The app is now deployed on Heroku.


## Local development

Prerequisites:
- IDE of your choice with:    
    - installed [Python 3](https://www.python.org/downloads/) and  
    - installed [pip](https://pypi.org/project/pip/), 
- created [Gmail](https://mail.google.com/) account with two-factor authentication enabled, and
- created [Stripe](https://stripe.com/) free account. 


_Note: the Terminal commands in the following steps assume a Windows environment and a Command Prompt shell. If you are using a different operating system and/or shell, the commands will need to be adapted to your environment._

If you want to work on this project locally, follow these steps:

1. Clone or download the MothRadar GitHub repository into your local IDE.

2. To install the project's dependencies, it is recommended to create a virtual environment to prevent the dependencies from being installed globally on your system.     
To create a virtual environment for your project, in the Terminal, in the project's root directory, enter:

    `python -m venv venv`

    and then activate the created virtual environment with

    `venv\Scripts\activate`

4. Upgrade `pip` if needed:

    `python -m pip install --upgrade pip`

3. Install the project dependencies using  the following command:

    `pip install -r requirements.txt`


4. In the root directory of the project (where the `manage.py` file is located), create a file named `env.py`.

    **Remember to check immediately that the `env.py` file is listed in your `.gitignore` file to prevent your sensitive data from being committed and pushed to GitHub.**

    Inside the `env.py` file, enter the following commands and variables:

    _Note: all variable values must be **in quotes**._

   ```python
    import os

    os.environ["DEVELOPMENT"] = "1"
    os.environ["LOCALHOST"] = "127.0.0.1"

    os.environ["SECRET_KEY"] =      # your secret key
    os.environ["EMAIL_ADDRESS"] =   # your Gmail email address 
    os.environ["EMAIL_PASSWORD"] =  # your Gmail two-factor authentication app password

    os.environ["STRIPE_PUBLISHABLE"] = # your Stripe Publishable Key 
    os.environ["STRIPE_SECRET"] = # your Stripe Secret Key
   ```

    _Note: setting the_ `"DEVELOPMENT"` _variable serves to set_ `DEBUG=True` _during development. If you want_ `DEBUG=False`, _simply omit the_ `"DEVELOPMENT"` _variable definition._ 

    Save the `env.py` file.


5. In the Terminal, run 

    `python manage.py makemigrations` 

    to create the migrations for your Django database, and then

    `python manage.py migrate`

    to apply the migrations to the database.


6. In the Terminal, run

    `python manage.py createsuperuser`

    When prompted, enter a username, email, password, and repeat password, to complete superuser creation.


  **The application can now be run locally using the following command:**

`python manage.py runserver`
***

## Code validation

### HTML 

Validated using [W3C Markup Validation Service](https://validator.w3.org/).   
Issues found:
1. Register form -  "Element **ul** not allowed as child of element **small** in this context."
2. Password Reset Confirm form -  "Element **ul** not allowed as child of element **small** in this context."
3. Password Change form -  "Element **ul** not allowed as child of element **small** in this context."

These issues are related to the way Crispy Forms handles the HTML rendering of the respective Django forms.

Given that:
- these errors are not related to author-written code in any way,
- no display errors have been observed in rendering of the forms concerned in any of the test browsers, and
- elimination of the errors would imply dispensing with Crispy Forms altogether or at least a "manual" redesign of the forms concerned, which is time-prohibitive,   
it has been decided to proceed with deployment regardless of the aforementioned errors.


### CSS

Validated using [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).   
No issues were found.

### JS

Validated using [JSHint](https://jshint.com/).   
No issues were found.

### Python 
Validated using [PEP8 online](http://pep8online.com/).   

Issues found: "Line too long" in lines 111 and 113-115 of `settings.py`:
```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]
```
Considering my insufficient experience as well as the absence of an unambiguous confirmation that configurations like these should also be split into concatenated multi-line strings, this snippet has been left as-is regardless of the raised pep8 errors. 


## Testing

**Note to Assessors: to enable assessment of the backend/admin side of the app (if needed), a 'staff' account with read-only privileges has been created:**  

- **_username_: demoadmin**   
- **_password_: admintest456**


### User stories

_Note: As detailed in the UX section above, User Stories 11 and 12 (editing and deleting of user's comments) have not been implemented in this version and are therefore not tested._

All user stories have been tested. 

The following issues have been observed:
***
**Issue #1: Search filter view reverts to all tickets view upon "Next page" click.**

_Analysis: Upon Search, the queryset is set correctly (the number of pages is correct), but requesting the next page deletes the search call and reverts to the default queryset (and number of pages) of TicketListView._

_Solution: I have tried to override the default pagination (paginate_by=5) if search is performed by using paginate_queryset, but all my attempts have been unsuccessful._

**Conclusion: the issue will need to be fixed in a later version of the app.**
***
**Issue #2: Ticket list view and detail view needlessly display time (H:MM) of ticket creation.**

_Analysis: In a late stage of development, the date_created field format in the Ticket model has been changed to DateTimeField. However, in the ticket_list and ticket_detail templates no filter was added to filter out the time part._

_Solution: Add filter (display only date) to the display of object.date_created in the ticket_detail template and of ticket.date_created in the ticket_list template._  

_Validation: Revalidate HTML code of ticket_list.html and ticket_detail.html. Re-check display of concerned data in ticket list and ticket detail views._  

Outcome: Fix implemented, HTML code successfully revalidated, display of ticket list and ticket detail views checked. Issue has been fixed.

**Conclusion: Issue #2 is fixed and can be closed.**
*** 


### Features

#### Navbar 
1. Check that the navbar contents change dynamically dependent on whether the user is logged in or not.
2. Check that all links are working in both cases.
3. Check that the Create ticket button is not present if user is not logged in.

_All Navbar features have been tested successfully. No issue was found._

#### Landing page
1. Check that the landing page renders properly.
2. Check that the four information cards are responsive (colour highlight, toggle expand) upon clicking or hovering.
3. Check that the information cards display the desired textual information.
4. Check that the login and register anchors are only present if a user is not logged in.
5. Check that the registration and login anchors, when present, are functional.
6. Check that the footer anchor is functional and opens the link in a new tab.

_All Landing page features have been tested successfully. No issue was found._

#### Ticket list view, sorting and search
1. Check that the ticket list view displays all expected information.
2. Check that pagination is present.
3. Check that all pagination links (First, Prev, Next, Last) work as expected.
4. By going to the admin pages, check that the total list of tickets displayed corresponds to the total list of tickets in the database.
5. Check that the search box and sidebar links are rendered correctly.
6. Check that the sidebar view "My tickets" is only present if a user is logged in and then contains the correct number of tickets raised by that user.
7. Check that the default view in ticket list sorts tickets descending by date created.
8. Check that the "Most recent" view sorts tickets as expected.
9. Check that the "Most upvoted" view sorts tickets as expected.
10. Check that the "Bugs only" and "Features only" views filter tickets as expected.
11. Check that the search functionality works as expected. 

_All Ticket list view features have been tested successfully. No issue was found except as related to point 11, which is already highlighted in **Issue #1**._

_Note: during testing it has been observed that the Ticket view on the admin pages only logs the ticket title, which makes it difficult to check the number of tickets per author or type. Therefore an adjustment has been made to tickets/models.py to display all details (except date_created and description) in the admin pages. The corresponding Python code has been revalidated successfully._


#### Ticket detail view

1. Check that the Ticket detail view displays all ticket information, including upvotes count.
2. Check that the Upvote button is only present if a user is logged in. 
3. Check that the upvote button is greyed out if the logged-in user has already upvoted the ticket.
4. Check that the comments text area and Post comment button are only present if a user is logged in.
5. Check that existing comments (if any) are displayed regardless if a user is logged in or not.
6. Check that the "Edit ticket" button is only present if the logged-in user is the ticket author AND the ticket is in status "OPENED". If the edit button is not present, check that a manual (via URL) attempt to access the edit route for the ticket results in a "Not found" error.
7. If the Edit ticket button is available, check that it is possible to edit the title, description and ticket type fields of the ticket, and that all fields are mandatory. Check that, upon submission, the modified ticket details are updated. 

_All Ticket list view features have been tested successfully. No issue was found._

#### Upvoting system

1. Check that the Upvote button is displayed with a lock icon for Feature tickets (if not yet upvoted by the current logged-in user). Check that the lock icon is not displayed for Bug tickets under identical conditions.
2. Check that the Upvote button is greyed out and insensitive if the current logged-in user has already upvoted the ticket.
3. In a Bug ticket, upon clicking the Upvote button, check that the button becomes greyed out, a success message is displayed next to the button, and the upvote counter is increased by 1. Upon a repeated click, check that a message "Already upvoted." is displayed.
4. In a Feature ticket, upon clicking the Upvote button, check that a modal opens informing the user that this is a paid service (including the price) and offering the user the options to cancel or to proceed.
5. If the user selects Cancel, check that the modal closes, and the ticket's upvote count and the availability of the upvote button remain unchanged.
6. If the user selects Proceed, check that the browser redirects to the Payment Processing form.
7. Check that the Payment Processing form is displayed as expected.
8. Check that, upon entering of invalid card data:
    - card number shorter than 12 digits, or
    - CVV shorter than 3 digits, or
    - expiry month in the past,

    and clicking the Submit payment button, a corresponding error text is presented to the user next to the Submit payment button.   
9. Check that, upon entering valid card data and clicking Submit payment, if the payment is unsuccessful (e.g. due to card processing errors), a red alert banner is displayed below the Navbar. Check that the alert banner can be closed.
10. If the payment is successful, check that the browser redirects to the upvoted ticket's detail view, a green alert closable banner is displayed below the Navbar, the upvote button is greyed out, and the upvote count has been increased by 1.

_The upvoting system has been tested successfully. No issue was found._

#### Comments system

1. In the Ticket detail view, if a logged-in user attempts to submit a comment without entering any content into the comment text area, check that an information message is displayed next to the Submit comment button.
2. If a logged-in user submits a non-empty comment, check that the comment becomes displayed at the bottom of the existing comments (if any) and highlighted in green.
3. Upon page refresh, check that the newly submitted comment is displayed without highlight.
4. Check that the existing comments are sorted from newest at the top.
5. Check that there is a "No comments yet." paragraph if no comments have been submitted for the ticket yet. 

_The comments system has been tested successfully. No issue was found._

#### User handling
1. In the Register view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.
2. In the Profile Update view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user. Check that it is not possible to change the username if a user of the same name already exists.
3. In the Password Change view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.
4. In the Password Reset Confirm view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.

_The user handling system has been tested successfully. No issue was found._

#### Defensive design
1. If the user is not logged in, check that a "manual" (via URL editing) attempt to access: 
    - ticket create view,
    - ticket edit view, 
    - profile view, 
    - upvote view (for Bug tickets), or
    - upvote-feature view (for Feature tickets)

    will redirect to login view.

2.  If a logged-in user attempts to manually (via URL) access the upvote-feature route for a ticket they have already upvoted, and they submit valid payment data, check that the browser redirects to the concerned ticket, a yellow alert closable banner is displayed below the Navbar, and the upvote count remains unchanged.   


### Responsive design

For all tests listed until now, Google Chrome has been used as the test browser. No issues except the already documented ones have been identified.

All relevant user stories have been retested using:
-  Mozilla Firefox, 
- Microsoft Edge,
- Google Chrome Developer Tools emulated device mode - iPhone X.

Particular attention was paid to the three forms (Register form, Password Reset Confirm form, Password Change form) which returned an error during HTML code validation.  

On Mozilla Firefox, no new issue was observed. The three aforementioned forms rendered without issues.

On Microsoft Edge, no new issue was observed. The three aforementioned forms rendered without issues.

On Google Chrome emulated device mode, the following issues were observed:
***
**Issue #3: The footer bar is displayed as a strip, not touching the bottom of the screen, and the footer text is stretching outside of it.**

_Analysis: Due to the narrow(er) screen width, the footer text splits into two lines. Since the current footer CSS height (4vh) is insufficient to cover two lines, the resulting text cannot be contained in the footer._

_Solution: in style.css, change the footer property to `min-height:4vh`, which will keep its current height on large screens but enable it to stretch if necessary on smaller ones._   

_Validation: Revalidate CSS code of style.css. Perform collectstatic and push the code to Heroku. Re-check display of footer on test screen and on desktop screen._   

Outcome: CSS code revalidated OK. Collectstatic performed and code redeployed to Heroku. Display unchanged on desktop, issue no longer present on test screen. Issue resolved.

**Conclusion: Issue #3 is fixed and can be closed.**
***
**Issue #4: In ticket list view, the search button is pushed to the second line, not aligned with the search box.**   

_Analysis: the search box width on small screens was set to Bootstrap_ `col-9 col-lg-8`, _which, together with margin settings, caused the button to wrap onto a second line on small screens._

_Solution: in ticket__ _list.html, modify the search box width to_ `col-8 col-md-9 col-lg-8` _to remove the issue on small screens and keep the good display on medium and large+ screens._  

_Validation: Revalidate HTML code of ticket__ _list.html. Re-check display of search box and buttons on test screen and on medium and desktop screens._ 

Outcome: HTML code revalidated OK. Display unchanged on medium and larger screens, issue no longer present on test screen. Issue resolved.   

**Conclusion: Issue #4 is fixed and can be closed.**
***
**Issue #5: In the slide-down menu, the Create ticket button is abnormally wide (full screen width) with an unwanted left margin.**   

_Analysis: In base.html, the current Bootstrap margin styling of the Create ticket button (_`mt-5`_) only catered for the display on desktop screens. This needs to be adjusted for screens of lower width._

_Solution: in base.html, modify the Create ticket button Bootstrap styling to_ `mr-auto px-2 ml-lg-5` _to keep the button appearance on desktop screens, but to remove the unwanted margin and reduce the button width on smaller screens._   

_Validation: Revalidate HTML code of base.html. Re-check display of Create ticket button on test screen and on larger screens._ 

Outcome: HTML code revalidated OK. Create ticket button isplay unchanged on large+ screens, issue no longer present on test screen and sizes below large. Issue resolved.
**Conclusion: Issue #5 is fixed and can be closed.**
***

**Issue #6: The upvote message unexpectedly pushes the Upvote button to the beginning of a new row.**   
_Analysis: On large screens this issue is not visible, but on small widths the screen is not wide enough to contain the upvote count, the message, and the upvote button on one line._

_Solution: in upvotes.html, add a Bootstrap class of_ `d-none d-sm-inline` _to the upvoteMessage span, to keep the message hidden on small screens and prevent the button from being pushed to another row._ 

_Validation: Revalidate HTML code of upvotes.html. Re-check display of upvote message and Upvote button on test screen and on larger screens._

Outcome: HTML code revalidated OK. Issue no longer present on test screen, behaviour unchanged on larger screens. Issue resolved.
**Conclusion: Issue #6 is fixed and can be closed.**
***
**Issue #7: The inline message for erroneous payment data is broken across two lines.**   
_Analysis: On large screens this issue is not visible, but on small widths the screen is not wide enough to contain the whole the whole error message in one row, and the existing Bootstrap margin of `ml-3` looks awkward._

_Solution: in payment.html, modify the Bootstrap class of the stripe-error-message span to_ `d-block d-md-inline ml-md-3` _to force the whole message to be displayed below the button on small screens and to apply the margin only on screens from medium above._ 

_Validation: Revalidate HTML code of payment.html. Re-check display of payment error message and payment button on test screen and on larger screens._

Outcome: HTML code revalidated OK. Issue no longer present on test screen, behaviour unchanged on medium screens and above. Issue resolved.

**Conclusion: Issue #7 is fixed and can be closed.**
***
All five issues raised during Responsive design testing (Issues #3 - #7) have been fixed and closed. No new issues have been identified. The rendering of HTML forms that had raised errors during HTML validation shows no issues.

## Technologies Used

Languages:

- HTML for page structure and content;
- CSS for content styling;
- JavaScript for HTML DOM manipulation, Ajax server requests and Stripe payment processing;
- Python 3 for application logic;

Framework:
- [Django](https://www.djangoproject.com/) framework (v3.0.5) for application backend, development database provision (SQLite3), routing and template manipulation; 

Libraries:
- [Bootstrap](https://getbootstrap.com/) was used for responsive design, styling, navigation bar, buttons, alerts and modal implementation;
- [jQuery](https://jquery.com/) for easier DOM manipulation and for Stripe payment;
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to facilitate HTML rendering of Django forms;
- Fonts were obtained from [Google Fonts](https://fonts.google.com/);
- Icons were obtained from [FontAwesome](https://fontawesome.com/);

Development:
- [Visual Studio Code](https://code.visualstudio.com/) was used as the IDE for development and Git version control;
- [GitHub](https://github.com/) was used for source code storage;
- Google Chrome Developer Tools were used for development and testing, debugging and as a styling aid;
- [Travis CI](https://travis-ci.org/) for continuous integration;

Code validation tools:
- [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
- [JSHint](https://jshint.com/) was used to validate JavaScript code;
- [PEP8 online](http://pep8online.com/) to validate Python code;

Deployment:
- [WhiteNoise](http://whitenoise.evans.io/en/stable) to facilitate Django static files serving on Heroku;
- [Heroku](https://www.heroku.com/) for application online deployment and production database provision (PostgreSQL);


Utilities:
- [wireframe.cc](https://wireframe.cc/) for wireframe creation;
- [W3schools.com Color Converter](https://www.w3schools.com/colors/colors_converter.asp) was used to convert colours between default, HEX and RGB for CSS coding purposes;
- [Autoprefixer CSS online](https://autoprefixer.github.io/) was used for correct vendor prefixing of CSS styles where required;
- [convertio.co](https://convertio.co/) was used to convert favicon image from SVG to PNG;
- [Favicon.io](https://favicon.io/) was used for favicon creation;

External (third-party) services:
- [Gmail](https://mail.google.com/) for sending of Password Reset messages to users;
- [Stripe](https://stripe.com/) v2 was used for credit card payment processing.


## Credits

### Code

#### HTML
1. The solution to highlight the currently active link in the sidebar within the ticket_list.html template (`{% if path == ... %}`) was found on [Stack Overflow](https://stackoverflow.com/).
2. The custom script to pass the Stripe Publishable Key into JavaScript (in upvotes.html) was obtained from the Code Institute course videos.   

#### JavaScript
The complete Stripe payment processing script (stripe.js file) was obtained from Code Institute course videos.

#### Python / Django
MothRadar being my first independent Django project, I had to still tackle the basics of Django together with building a full-fledged app. Thus I had to rely heavily on external resources, primarily on [Corey Schafer's YouTube Django series](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) tutorial and then on Code Institute course videos as well.   
While I never wanted to just copy-paste any code, especially not without understanding it, in the beginning stages of my project (the `users` app and the initial stage of the `tickets` app) I was coding along with the tutorials a lot, while adapting the code to the specific needs of my app. In later stages I relied mostly on Django documentation and occasionally on Stack Overflow to implement the desired functionality.    
Thus, while the concrete app implementation is definitely my own, the significant influence of Corey's videos is inevitable. This includes the idea to use Bootstrap cards to display the main items (tickets and comments), a sidebar, as well as the use of Crispy Forms to render Django forms.   
I have honestly tried to do all the coding as independently as I could once my understanding of Django and of documentation broadened, but at this stage of my coding education building a full Django app of this size completely independently would have been impossible, especially in the given timeframe. 

### Media
- Favicon image was obtained from [publicdomainvectors.org](https://publicdomainvectors.org/).


### Acknowledgements
Above all I would like to thank Chris (**ckz8780**) who helped me immensely on this project with his knowledge of Django. While never providing me with complete solutions, on multiple occasions he was able to point me to the right direction to look for them. He also helped me debug the Stripe payment functionality when I got completely stuck. Thanks, Chris!

Also, many thanks to all my fellow CI Slack members who also helped either by pointing me to various Django resources, by sharing their experiences, having walked the same path before me, or simply by encouraging me when I lost my momentum. **Anna**, **Jo**, **Simen**, **Johan** and **Anthony** - I owe you all bigtime!!  

Finally, a special THANK YOU to my mentor Narender, who always patiently tries and manages to find a way to push my limits just that tiny bit further. :) 



