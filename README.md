"# djangorestframework_noteapp_restapi" 

DJango Rest Framework and MongoDB : Rest API (GET, POST, PUT, DELETE)


Django REST Framework ... Django REST framework is a powerful and flexible toolkit for building Web APIs. Some reasons you might want to use REST framework:.

Project setup
Create a new Django project named tutorial, then start a new app called quickstart.

# Create the project directory
mkdir note_app
cd note_app

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject note_app .  # Note the trailing '.' character
cd tutorial
django-admin startapp api
cd ..


UI and UX : HTML and CSS