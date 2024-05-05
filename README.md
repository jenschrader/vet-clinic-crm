# 🐱 Veterinary Clinic Management System 🐶

## Overview 💡
This web-based application is designed to assist small veterinary clinics in managing basic information related to their clients and pets. The software targets small vet clinics and aims to provide functionalities such as login/logout, registration, and simple CRUD (Create, Read, Update, Delete) operations for managing client and pet information.

## Local Installation ⚙️
As this project is hosted on PythonAnywhere, it's not directly cloneable in the traditional sense, but you can set it up locally for development or testing purposes. Follow these steps to get started:

### 1. Clone the Repository:
Begin by cloning the project repository to your local machine. Open a terminal or command prompt and run:
```console
git clone https://github.com/jenschrader/django-crm.git
```
### 2. Set Up a Virtual Environment: 
Navigate to the project directory and set up a virtual environment so that dependencies are isolated:
```console
cd vet-clinic-crm
python -m venv env
```
### 3. Activate the Virtual Environment:
Commands may differ depending on your machine or preferred terminal/console. We use GitBash - the following command works for GitBash consoles:
```console
source env/scripts/activate
```
### 4. Install Dependencies:
Using pip, install the requirements.txt file:
```console
pip install -r requirements.txt
```
### 5. Modify Local Settings:
**Note: Make sure to have MySql installed on your machine. You will need to set up your local database before modifying.**
To configure the project to target locally, you must modify the `settings.py` file. Here is an example of what code to alter:
```python
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_local_database_name',
        'USER': 'your_database_username',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
```
### 6. Migrate Database:
Run migrations to set up your local database schema:
```console
python manage.py migrate
```
### 7. Create Superuser (Optional):
If you want to access the Django admin interface locally, create a superuser:
```console
manage.py createsuperuser
```
### 8. Run the Development Server:
Finally, you can start the Django project by running the following command:
```console
python manage.py runserver
```
Once running, you can access the application by navigating to `http://localhost:8000` in your web browser.

## PythonAnywhere 🔗

To access the application:

1. Visit https://vetcrm.pythonanywhere.com/
2. Sign up for an account or log in with existing credentials.
3. Once logged in, you will have access to the application's functionalities based on your permission level.

## Features ✨
- User Authentication (login/logout)
- User Registration 
- CRUD operations for managing client information
- CRUD operations for managing pet information
- Responsive design for easy use on various devices
- Differing permission levels based on account type

## Technologies 💻
- **Django**: Backend web framework
- **HTML/CSS**: Frontend markup and styling
- **Bootstrap 5**: Frontend framework for responsive design
- **Bootswatch Minty theme**: Styling theme for Bootstrap
- **jQuery DatePicker**: JavaScript plugin for date selection
- **JavaScript DataTables**: JavaScript plugin for interactive tables
- **MySQL**: Relational database management system
- **PythonAnywhere**: Hosting platform

## Usage 🚀
### Logging in/Logging out:
- Access the login screen by visiting the application URL.
- Enter your username and password (if you have an existing account)
- Click the login button to access the dashboard/home screen.
- If login fails, an error message indicating the cause of failure will appear.
- To logout, click the "logout" link in the navigation bar.

### Signing Up:
- If you don't have an account, click the "Sign up here" link on the login screen (or in the navigation bar).
- Fill out the signup form with your details.
- If there are any errors, a message will alert you with the issue.
- Upon successful signup, you will be automatically logged in with limited permissions.

### Managing Clients:
- On the dashboard/home screen, view a table of clients.
- Click the "New Client" button to create a new client.
- Click the "View" button located within the table to see details about a specific client and their associated pets (if any).
- On the client view page, you can edit or delete clients.
- Deleting a client will delete any pets associated with that client.
- Limited permission users cannot create or delete clients.

### Managing Pets:
- On the client view page, you can add, edit, or delete pets associated with the client.
- Pets can be added, edited, or deleted individually.
- Deleting a pet associated with a client does not delete the client record.

## Permissions Levels 🔒
The application implements different permission levels based on the user's account type:

- **Limited Permissions**: Users with limited permissions can view clients and pets, edit clients, add new pets, edit existing pets, and delete pets.
- **Administrator**: Administrators have full access to all functionalities.

These permission levels ensure appropriate access control and data security within the application.

## License 📋
This project is licensed under the MIT License.

## Future Development 🤔💭
While the current version of the application provides essential functionalities for managing veterinary clinic information, future development plans include:
- Implementing multi-tenancy.
- Expanding application functionally by creating additional features such as appointment scheduling and medical record management.
- Enhancing user interface and user experience.
- Improving performance, security, and scalability of the application.

# 🐈 🐕
