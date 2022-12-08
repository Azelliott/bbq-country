# BBQ Country

BBQ Country is a restaurant offering the best barbecue in town. Our menu features a wide variety of mouthwatering dishes, including pulled pork, ribs, 
burgers and chicken on variety of ways. We also offer sides and desserts to satisfy any craving.

## Project Description
BBQ Country is a restaurant website that showcases the mouth-watering barbecue dishes available at our restaurant. The site features a main page with a brief overview of our restaurant, a menu page where users can browse through our delicious dishes, and a gallery page where users can see photos of our restaurant and food.

Users can log in and book a date and time to dine at our restaurant. The website has been tested on various operating systems and browsers to ensure compatibility and a seamless user experience.

![Screenshot of BBQ Country website](static/image/screenshots/bbq-index.png)

### View the live preview [here](https://bbq-country.herokuapp.com/)
(NOTE: Hold Ctrl and click the link to open in new tab)

## Table of content: 
 - [Technologies Used](#Technologies-Used)
 - [Features](#Features)
    * [Overview](#Overview)
    * [Main Page](#Main-Page)
    * [Menu](#Menu)
    * [Gallery](#Gallery)
    * [About Us](#About-Us)
    * [Reviews](#Reviews)
    * [Booking Form](#Booking-Form)
    * [Reservations](#Reservations)
    * [Sign in and Sign out](#Sign-in-and-Sign-out)
    * [Admin Panel](#Admin-Panel)
 - [Testing and Validation](#Testing-and-Validation)
   * [OS and Browser Tests](#OS-and-Browser-Tests)
   * [Unit Testing](#Unit-Testing)
   * [Validation](#Validation)
   * [Running Automated Tests](#Running-Automated-Tests)
 - [Deployment](#Deployment)
    * [Local Machine](#Local-Machine)
    * [Heroku](#Heroku)
 - [Attributions](#Attributions)



## Technologies Used

### Core Technologies
This project is built with the following technologies:

* [Django](https://www.djangoproject.com/) 4.1.3 - A web framework for Python
* [Bootstrap](https://getbootstrap.com/) 5.1.3 - A CSS framework for styling and layout
* [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) - A layout system for building responsive and flexible web pages
* [PostgreSQL](https://www.postgresql.org/) - Database Engine

### Libraries
[Starability](https://github.com/LunarLogic/starability) - Star rating library in pure HTML and CSS

[Django Phone Number Field](https://pypi.org/project/django-phonenumber-field/) - A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers. python-phonenumbers is a port of Google’s libphonenumber library, which powers Android’s phone number handling.

[Bootstrap Datepicker](https://bootstrap-datepicker.readthedocs.io/en/latest/) - Bootstrap-datepicker provides a flexible datepicker widget in the Bootstrap style.

[jQuery Timepicker](https://timepicker.co/) - jQuery Timepicker can parse the most used time representations allowing you and your users to enter time using their prefered way for writing it.


## Features

### Overview
* A main page with a brief overview of our restaurant.
* A menu page where users can browse through our dishes.
* A gallery page with photos of our restaurant and food.
* About us page with short description of restaurant style and dishes.
* User login and booking system for making, updating or deleting the reservations.
* Reviews page where users can post a review with a rating and see other reviews.

### Main Page
The main page features a minimalist design, containing only high-res background 
and few (cheesy) slogans.
Header will show different options depending on whether user is authenticated or not. Logout button shows active username.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-index.png)

### Menu
The menu page displays a list of barbecue dishes on offer. It features a image for each type of dish, such as pulled pork, ribs, and chicken, as well as a title. I didn't want to get into pricing and descriptions to keep it clean, but 
it can be easily added to each card if needed.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-menu.png)

### Gallery
Continuing in minimalist style, the gallery page showcases photos of our delicious food and restaurant atmosphere. It includes a carousel of photos, each photo is fullscreen.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-gallery.png)


### About Us
About Us page contains a short description of the restaurant.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-about.png)

### Reviews
Authenticated users can leave a review for the restaurant on the reviews page. They can also view all reviews left by other users.
Each post has username and a timestamp, posts are sorted in ascending order.
There is a 1500 character limit.
Star rating is implemented with starability CSS library.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-reviews.png)
![Screenshot of BBQ Country website](static/image/screenshots/bbq-add-review.png)

### Booking Form
Authenticated users can book a time and date of their visit.
Form has required fields and it also checks the validity of information entered.
For example email and phone number have to be in correct format.
There is also date picker that has some defensive coding implemented, for example users can't book a date in the past.
Form also has a timepicker with predefined working times.
Number of people field requires minimum of 1, has to be number etc.
Application will show the user messages on success/fail.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-booking.png)

### Reservations
Not only can authenticated users see their reservations, they can also make updates 
or cancel (delete) them altogether.
Each entry has Edit and Delete buttons. 
Edit button will redirect the user to main booking form and prefill the fields with selected records info.
Delete button will, surprise.. delete the info from DB.
Application will show the user messages for success/fail.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-reservations.png)

### Sign in and Sign out
Sign in and sign out forms will show the user messages for success/fail.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-signin.png)
![Screenshot of BBQ Country website](static/image/screenshots/bbq-signout.png)


### Admin Panel
The admin has the ability to view, update, and delete all reservations and reviews on the admin panel. He can also add or remove users or change their details.
![Screenshot of BBQ Country website](static/image/screenshots/bbq-admin.png)

## Testing and Validation

### OS and Browser tests
This project has been tested on the following operating systems and browsers:

* Windows 10 
   - Chrome 
   - Firefox 
* Fedora Silverblue Linux 
   - Chrome
   - Firefox
* iPad OS on iPad Air 
   - Safari

### Unit Testing
Unit tests are located in the restaurant/test repo folder. These tests cover the following features:

#### Unauthenticated test:

* Test GET method on unauthenticated views - pages that should load correctly 
   - Index 
   - Menu 
   - Gallery 
   - Reviews

* Test GET method on unauthenticated views - pages that should redirect to login form 
   - Booking 
   - My Reservations
   - Add Review

#### Sign up form test:
* Test signup form status code
* Test signup form create user - valid
* Test signup form missing username - invalid
* Test signup form miss-matching passwords - invalid
* Test signup form missing password - invalid

#### Log in form
* login form status code
* login form with valid user
* login form with invalid user

#### Booking form
* Test booking form for unauthenticated user, user should be redirected to login page
* Test booking form for authenticated user
* Test booking form with valid data, user should be redirected to my_reservations page after successful booking

<br>

![Screenshot of BBQ Country website](static/image/screenshots/bbq-unit-tests.png)


### Validation
The website has been tested for HTML and PEP8 validation.


#### PEP8
[CI PEP8 Validator](https://pep8ci.herokuapp.com/#) - Code institute validator

Site is 99.9% PEP8 compilant - it only failed in 2 instances on "line too long" but trying to split the line 
brakes the code so I left it like that.

First instance:
![Screenshot of BBQ Country website](static/image/screenshots/validations/bbq-pep8-1.png)
![Screenshot of BBQ Country website](static/image/screenshots/validations/bbq-pep8-1.1.png)

Second instance:
![Screenshot of BBQ Country website](static/image/screenshots/validations/bbq-pep8-2.png)
![Screenshot of BBQ Country website](static/image/screenshots/validations/bbq-pep8-2.2.png)


#### HTML
[W3 HTML Validator](https://validator.w3.org/nu/) - W3 HTML Online Validator

Site passes 100% on HTML Validation

![Screenshot of BBQ Country website](static/image/screenshots/validations/bbq-html.png)


### Running Automated Tests
To run the automated tests for this project, run the following command:
<br>

```
python manage.py test
```

## Deployment

### Local Machine

To deploy this project on your own server/local machine, follow these steps:

1. Install Python and PostgreSQL on your server.
2. Clone the repository from GitHub:

```
git clone https://github.com/Azelliott/bbq-country.git
```

3. Install the project dependencies:
```
cd bbq-country
pip install -r requirements.txt
```


4. Set up the database and create a superuser:
```
python manage.py migrate
python manage.py createsuperuser
```

5. Start the server:
```
python manage.py runserver
```

6. Open a web browser and go to `http://localhost:8000` to access the website.

### Heroku
1. Create a new Heroku app and a database ( DB can be a separate service )
2. Connect the app to the GitHub repository

3. Create env.py file and set up config vars:

```
SECRET_KEY: secret key for Django

DEBUG: set to False in production

ALLOWED_HOSTS: hostname of the Heroku app

DATABASE_URL: URL of the PostgreSQL database

```


## Attributions

Site images found on [Unsplash](https://unsplash.com/)
Favicon is from  