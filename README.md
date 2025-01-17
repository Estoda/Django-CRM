# CRM App

A Customer Relationship Management (CRM) application built using **HTML**, **CSS**, **Bootstrap**, **Python**, **Django**, **MySQL**, **Git**, and **GitHub**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project is a CRM application that helps manage customer records efficiently. It allows adding, updating, and deleting customer details, among other functionalities.

---

## Features

- Add, view, update, and delete customer records.
- User authentication and registration.
- Responsive design with Bootstrap.
- Integration with MySQL for database management.
- Modular structure with reusable templates.

---

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: MySQL
- **Version Control**: Git and GitHub

---

## Project Structure

CRM/
├── CRM/ # Main Django project directory
│ ├── **init**.py # Initializes the Django project as a Python package
│ ├── asgi.py # ASGI configuration for asynchronous support
│ ├── settings.py # Main project settings
│ ├── urls.py # Main project URL routing
│ ├── wsgi.py # WSGI configuration for deploying the project
│ ├── templates/ # Global templates (optional)
│ ├── base.html # Base template with shared layout
├── website/ # Main app directory
│ ├── migrations/ # Database migrations folder
│ │ ├── **init**.py # Initializes the migrations as a package
│ │ ├── 0001_initial.py # Auto-generated migration file
│ ├── templates/ # Templates specific to the `website` app
│ │ ├── add_record.html # Page for adding new customer records
│ │ ├── base.html # Shared base template for the app
│ │ ├── home.html # Home page
│ │ ├── navbar.html # Navigation bar template
│ │ ├── record.html # Page to view individual records
│ │ ├── register.html # User registration page
│ │ ├── update_record.html # Page to update existing records
│ ├── **init**.py # Initializes the app as a Python package
│ ├── admin.py # Admin site configuration for the app
│ ├── apps.py # App configuration
│ ├── forms.py # Forms for user input handling
│ ├── models.py # Database models for the app
│ ├── tests.py # Test cases for the app
│ ├── urls.py # URL routing specific to the `website` app
│ ├── views.py # Views that handle user requests and responses
│ ├── mydb.py # Custom database handling logic (optional)
├── manage.py # Django management script
├── requirements.txt # Python dependencies for the project
├── .gitignore # Files and directories to ignore in Git
├── README.md # Project documentation

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd CRM
   ```
