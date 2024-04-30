# 🐱 Veterinary Clinic Management System 🐶

## Overview 💡
This web-based application is designed to assist small veterinary clinics in managing basic information related to their clients and pets. The software targets startups and aims to provide functionalities such as login/logout, registration, and simple CRUD (Create, Read, Update, Delete) operations for managing client and pet information.

## Installation 🔗

As this project is hosted on PythonAnywhere, it's not directly cloneable in the traditional sense. To access the application:

1. Visit https://vetcrm.pythonanywhere.com/
2. Sign up for an account or log in with existing credentials.
3. Once logged in, you will have access to the application's functionalities based on your permission level.

## Features ✨
- User authentication (login/logout)
- User registration 
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

## Usage ⚙️
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
- Implementing additional features such as appointment scheduling and medical record management.
- Enhancing user interface and user experience.
- Improving performance, security, and scalability of the application.

# 🐈 🐕
