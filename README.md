# Installation

This guide assume that you have already installed postgresql

### Install environment dependencies

    sudo apt-get update
    sudo apt-get install python-dev libpq-dev

### Install and create virtualenv

    sudo apt-get install virtualenv
    virtualenv /path/to/folder/env_name

Activate the virtualenv

	source /path/to/folder/env_name/bin/activate

### Install Dependencies (requirements.txt)

	pip install -r requirements.txt

### Configure PostgreSQL

	sudo su -s postgresa
	createdb glife_db

Now we have to configure the database settings in local_settings.py

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': 'glife_db',
	        'USER': 'the_user',
	        'PASSWORD': 'the_password',
	        'HOST': '127.0.0.1',
	        'PORT': '5432',
	    }
	}

### Running migrations

	python manage.py makemigrations
	python manage.py migrate

Finally, if everything it's fine, run the server:

	python manage.py runserver
