# LittleLemon
## Overview
This is the capstone project of the [back-end developer](https://www.coursera.org/professional-certificates/meta-back-end-developer) specialization provided by Meta. 
It demonstrates the ability to work as a full stack software developer.

## Project Setup
### Install dependencies
Our project manages dependencies via [pipenv](https://pipenv.pypa.io/en/latest/). To install dependencies, please run the command 
```bash
pipenv install
```
inside the project directory to create the required virtual environment.

### Database Configuration
The project is based on [MySQL](https://www.mysql.com/) database. Before running the project, please install MySQL database on your machine, and ensure that there is a user called `root` without password, and a database called `littlelemon`. 
After installing the database, please run the migration commands to create the tables:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Admin and Data items
Before starting the server, please create a super user account using the command
```bash
python manage.py createsuperuser
```
and login via `/admin/`. Inside the `Menu` table, please insert the following entries using the admin interface:
| title           | price | inventory |
|-----------------|-------|-----------|
| Grilled Fish    | 8.50  | 20        |
| Greek Salad     | 5.00  | 50        |
| Bruschetta      | 6.50  | 25        |
| Pasta Carbonara | 6.50  | 25        |
| Lemon Dessert   | 4.50  | 10        |
### Starting the server
After the configuration steps, please run the command to start the web server:
```bash
python manage.py runserver
```
By default, the project binds to host `127.0.0.1` and listens to port `8000`. 

## Major Components
### The front end
To see our website, please visit our home page at `/restaurant/` using your web browser. You can navigate between webpages like "About", "Menu" through the header. 
#### Menu Items
The webpage `/restaurant/menu/` displays the menu items inside the database. By clicking the title, you can see the information and image of each single menu item.
#### Booking form
The `/restaurant/book/` site is a form which is submitted via `POST` method. Notice that the `BookingDate` field has to be a valid date like YYYY-MM-DD. When the form is submitted, the record will be added to the database.

### The APIs
The APIs are built with the [Django REST framework](https://www.django-rest-framework.org/). To access the APIs, one must be authenticated via a valid token. 

To test the APIs, please use tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to generate HTTP requests.
#### Getting the API token
The user registration step is simulated in the administration interface `/admin/`. Please login with the superuser account and add entries to the `Users` table.

After registration, the API token can be acquired by sending `POST` requests to the address `/restaurant/api-token-auth/`. The content of `POST` request should be a form with string fields `username` and `password` corresponding to registered users. 
#### Dealing with database records at JSON format
Our web application provides APIs for authenticated users, which supports retrieval or modification of database records. Depending on the case, to use these APIs, the access token generated from the previous step might need to be provided in the request.

Here's a list of supported APIs:
* `/restaruant/api/menu/`: Use `GET` method to retrieve a list of all menu items, or `POST` method to add a new item. Authentication is required for `POST` but not for `GET`. 
* `/restaurant/api/menu/<int:pk>`: Use `GET` method to retrieve a single menu item whose ID equals `pk`, or `PUT` method to modify the menu item. Authentication is required for `PUT` but not for `GET`. 
* `/restaruant/booking/tables/`: An API managed by the router in REST framework, through which you can retrieve a list of all booking orders via `GET` method, or add a new order via `POST` method. Authentication is always required for this API.
#### Rate limiting.
Our project applies throttling to limit the number of requests in a period of time. Generally, anonymous users are limited to 100 requests per day, while authenticated users are limited to 1000 requests per day.

### Unit Testing
To demonstrate the concept of unit testing, our project includes a simple test case to verify the integrity of a model class. For example, according to the string type conversion, a menu item with title `IceCream` and price `80` should have string format `IceCream : 80`.
