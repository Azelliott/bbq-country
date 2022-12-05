# BBQ Country

BBQ Country is a restaurant offering the best barbecue in town. Our menu features a wide variety of mouthwatering dishes, including pulled pork, ribs, 
burgers and chicken on variety of ways. We also offer sides and desserts to satisfy any craving.

## Project Description
***
BBQ Country is a restaurant website that showcases the mouth-watering barbecue dishes available at our restaurant. The site features a main page with a brief overview of our restaurant, a menu page where users can browse through our delicious dishes, and a gallery page where users can see photos of our restaurant and food.

Users can log in and book a date and time to dine at our restaurant. The website has been tested on various operating systems and browsers to ensure compatibility and a seamless user experience.

![Screenshot of BBQ Country website](static/image/screenshots/bbq-index.png)

### View the live preview [here](https://bbq-country.herokuapp.com/)
(NOTE: Hold Ctrl and click the link to open in new tab)
***
## Table of content: 
 - [Technologies Used](#Technologies-Used)
 - [Deployment](#Deployment)
    * [Local Machine](#Local-Machine)
    * [Heroku](#Heroku)
 - [Features](#Features)
    * [Overview](#Overview)
    * [Main Page](#Main-Page)
    * [Menu](#Menu)
    * [Gallery](#Gallery)
    * [About Us](#About-Us)
    * [Reviews](#Reviews)
 - [Testing and Validation](#Testing-and-Validation)
   * [OS and Browser Tests](#OS-and-Browser-Tests)
   * [Unit Testing](#Unit-Testing)
   * [Validation](#Validation)
   * [Running Automated Tests](#Running-Automated-Tests)
 - [Attributions](#Attributions)



## Technologies Used
***
### Core Technologies
This project is built with the following technologies:

* [Django](https://www.djangoproject.com/) 4.1.3 - A web framework for Python
* [Bootstrap](https://getbootstrap.com/) 5.1.3 - A CSS framework for styling and layout
* [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) - A layout system for building responsive and flexible web pages
* [PostgreSQL](https://www.postgresql.org/) - A databaOS and Browser Tests

### Libraries
[Starability](https://github.com/LunarLogic/starability) - Star rating library in pure HTML and CSS

## Deployment
***
### Local Machine

To deploy this project on your own server, follow these steps:

1. Install Python and PostgreSQL on your server.
2. Clone the repository from GitHub:

git clone https://github.com/Azelliott/bbq-country.git


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


## Features
***

### Overview
* A main page with a brief overview of our restaurant.
* A menu page where users can browse through our dishes.
* A gallery page with photos of our restaurant and food.
* About us page with short description of restaurant style and dishes.
* User login and booking system for making reservations.

### Main Page
The main page features a minimalist design, containing only high-res background 
and few (cheesy) slogans.


### Menu
The menu page displays a list of barbecue dishes on offer. It features a image for each type of dish, such as pulled pork, ribs, and chicken, as well as a title. I didn't want to get into pricing and descriptions to keep it clean, but 
it can be easily added to each card if needed.

### Gallery
Keeping up with minimalist style, the gallery page showcases photos of our delicious food and restaurant atmosphere. It includes a carousel of photos, each photo is fullscreen.

### About Us
About Us page contains a short description of the restaurant.

### Reviews
Authenticated users can leave a review for the restaurant on the reviews page. They can also view all reviews left by other users.
Star rating is implemented with starability CSS library.




### Admin Panel
The admin has the ability to view, update, and delete all reservations and reviews on the admin panel.


## Testing and Validation
***
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

Menu page: checks if the menu items are correctly displayed and have the correct format and content.

Gallery page: checks if the gallery images are correctly displayed and can be clicked to view a larger version.

Login page: checks if the login form is properly functioning and can be submitted without errors.


### Validation
The website has also been tested for HTML and PEP8 validation. 


### Running Automated Tests
To run the automated tests for this project, run the following command:
<br>

```
python manage.py test
```

## Attributions
***