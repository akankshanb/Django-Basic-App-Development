# Django-Basic-App-Development

# Quick install guide

Before you can use Django, you’ll need to get it installed. We have a complete installation guide that covers all the possibilities; this guide will guide you to a simple, minimal installation that’ll work while you walk through the introduction.

# Install Python

Being a Python Web framework, Django requires Python. See What Python version can I use with Django? for details. Python includes a lightweight database called SQLite so you won’t need to set up a database just yet.

Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager.

You can verify that Python is installed by typing python from your shell; you should see something like:

Python 3.x.y </br>
[GCC 4.x] on linux </br>
Type "help", "copyright", "credits" or "license" for more information. </br>

# Set up a database

This step is only necessary if you’d like to work with a “large” database engine like PostgreSQL, MySQL, or Oracle. To install such a database, consult the database installation information(https://docs.djangoproject.com/en/2.2/topics/install/#database-installation)

# Install Django

You’ve got three easy options to install Django:

Install an official release. This is the best approach for most users.
Install a version of Django provided by your operating system distribution.
Install the latest development version. This option is for enthusiasts who want the latest-and-greatest features and aren’t afraid of running brand new code. You might encounter new bugs in the development version, but reporting them helps the development of Django. Also, releases of third-party packages are less likely to be compatible with the development version than with the latest stable release.

# Verifying

To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:

>>> import django </br>
>>> print(django.get_version()) </br>
2.2

# Creating a project

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, cd into a directory where you’d like to store your code, then run the following command:

$ django-admin startproject mysite
