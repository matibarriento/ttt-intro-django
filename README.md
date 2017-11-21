Django Intro
============

This is the code companion for introduction to django. I separated all the steps in commits.

### First step
* Create virtualenv (optional but recommended)
* Create new folder
* Install django ```pip install django```

### Second step
* Run ```django-admin startproject ttt```

### Third step
* Run ```./manage.py startapp tracking```

### Fourth step
* Create a `template` folder inside `tracking`
* Add `tracking` to `INSTALLED_APPS` in `settings.py`
* Add `index.html` to `template`
* Add a view function inside `views.py`
* Bind the view with an url in `urls.py`
* Run `./manage.py runserver` to start the server

### Fifth step
* Add a model in `models.py`
* Save a new instance and return all in the view
* Show them in the html
* Run the migrations
    * `./manage.py makemigrations`
    * `./manage.py migrate`

### Sixth step
* Regiter the model in the `admin.py` 
* Create superuser runnnig `./manage.py createsuperuser`

### Seventh step
* Improve the admin

### Eighth step
* Separte `INSTALLED_APPS`
* Add `django_extensions`