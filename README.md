# car-dealership Using Django for Python

A website for a car business owner who wants to list their cars on their website and allow the user to come to the site and browse through all of the latest cars and featured cars, search and filter the cars by model or price, and make some inquiries about cars that are out for sale.
use a Bootstrap template and turn it into  Django project's front-end. I also be customizing the default Django admin panel and make it a feature-rich, good-looking admin area. Login with Google & Login with Facebook is the really smart way to attract users into our application.


- Make real project according to the client requirements
- Implement HTML/Bootstrap template & Customise Django Admin Panel
- PostgreSQL Database & Deploy it into Production Server
- Setup Virtual Environment
- Creating Django Apps
- Git
- Implementing HTML and Bootstrap
- PostgreSQL Database Setup
- Django Static Files & Media Files
- Django Admin Customisation
- Database Schema, Models and Migrations
- Implementing RichText Editor & Multi-Select Fields on Admin Backend
- Fetching Database Objects
- Pagination
- Search Functionality
- User Authentication
- Login with Facebook & Login with Google
- Send Emails
- Database Dump Data & Load Data (local & remote)
- Deploy on Heroku Server (Gunicorn, Whitenoise)
- Add Custom Domain


### `Installing Django`
To create a virtual environment:
    $ pipenv

To Install Django:
    $ pip install django

To upgrade:
    $ python -m pip install --upgrade pip

To create the project
    $ django admin startproject car_dealership .

To create App:
    $ python manage.py startapp pages

To make migration changes
    $ python manage.py makemigrations
    $ python manage.py migrate

To create static files
 $ python manage.py collectstatic
 
### `Starting the project`
    $ pipenv shell
    $ python manage.py runserver 

