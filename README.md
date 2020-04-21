# ipssihelp
python - django - ipssi 2020

[![License](https://img.shields.io/static/v1.svg?label=license&message=proprietary&color=blue)](https://img.shields.io/puppetforge/rc/:user.svg)


#### Creating a project
```bash
django-admin startproject jobboard
```

#### Creating the handler app
```bash
python manage.py startapp handler
```

#### Create a super user
First we’ll need to create a user who can login to the admin site. Run the following command:
```bash
python manage.py createsuperuser
```

#### Portainer
```bash
http://localhost:30033
```

#### pgAdmin
```bash
http://localhost:30032
```

#### Django administration
```bash
http://localhost:30031/admin/
```

#### Start project
```bash
git clone
docker-compose up
go to portainer : localhost:30033
user / pass
container : ipssi-python  petite flèche : >
connect
pip-compile requirements.in
pip install -r requirements.txt
cd ipssihelp
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigration
python manage.py migrate
python manage.py runserver 0:8000
```

#### Start LOCALY project
```bash
git clone
docker-compose up
docker-compose exec ipssi-python /bin/bash
pip-compile requirements.in
pip install -r requirements.txt
cd ipssihelp
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigration
python manage.py migrate
python manage.py runserver 0:8000
```
