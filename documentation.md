Cloning

echo "# django-website-rest-database" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/joelwembo/django-website-rest-database.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/joelwembo/django-website-rest-database.git
git branch -M main
git push -u origin main


For Ubuntu
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # For Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..

Virtual Environment

For Windows


(Insde the Project folder  at the root folder with manage.py)
python -m pip install --user virtualenv
virtualenv env    

for Lunix source env/bin/activate

For Windows env\Scripts\activate

The Env folder will propmt aside the path


next step

pip install django django-rest-framework djongo

django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart


# Data migation

python manage.py makemigrations
python manage.py migrate

Creating an admin user

python manage.py createsuperuser  or

python manage.py createsuperuser --database=pools specify the database


running

python manage.py runserver 0.0.0.0:5000

Prepare Requirement doc for all tools and lib

step 1 pip freeze 
step 2 pip freeze > requirements.txt


Managaning Multiple Database

python manage.py migrate --database=polls

python manage.py migrate --database=customers

