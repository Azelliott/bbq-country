![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# BBQ Country

A restaurant offering the best BBQ in town.

## Project Description

BBQ Country is a restaurant website that showcases the mouth-watering barbecue dishes available at our restaurant. The site features a main page with a brief overview of our restaurant, a menu page where users can browse through our delicious dishes, and a gallery page where users can see photos of our restaurant and food.

Users can log in and book a date and time to dine at our restaurant. The website has been tested on various operating systems and browsers to ensure compatibility and a seamless user experience.

![Screenshot of BBQ Country website](screenshot1.png)
![Screenshot of BBQ Country website](screenshot2.png)
![Screenshot of BBQ Country website](screenshot3.png)

## Technologies Used

This project is built with the following technologies:

* [Django](https://www.djangoproject.com/) - A web framework for Python
* [Bootstrap](https://getbootstrap.com/) - A CSS framework for styling and layout
* [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) - A layout system for building responsive and flexible web pages
* [PostgreSQL](https://www.postgresql.org/) - A database management system for storing data

## Deployment Steps

To deploy this project on your own server, follow these steps:

1. Install Python and PostgreSQL on your server.
2. Clone the repository from GitHub:

git clone https://github.com/Azelliott/bbq-country.git

Copy code

3. Install the project dependencies:

cd bbq-country
pip install -r requirements.txt

Copy code

4. Set up the database and create a superuser:

python manage.py migrate
python manage.py createsuperuser

Copy code

5. Start the server:

python manage.py runserver

Copy code

6. Open a web browser and go to `http://localhost:8000` to access the website.

## Features

* A main page with a brief overview of our restaurant.
* A menu page where users can browse through our dishes.
* A gallery page with photos of our restaurant and food.
* User login and booking system for making reservations.

## Testing and Validation

This project has been tested on the following operating systems and browsers:

* Windows 10 - Chrome, Firefox, Safari
* Fedora Silverblue Linux - Chrome, Firefox
* iOS on iPad Air - Safari

The website has also been tested for HTML and PEP8 validation. To run the automated tests for this project, run the following command:

python manage.py test
