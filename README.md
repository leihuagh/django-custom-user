# django-custom-user

Base Template for dockerised django app with Custom User extending AbstractUser. Clone the repo and use as the base for your project

## Properties
python version : 3.6.8

django version : 2.0.9

user model : extends Abstract user model extra field "life_motto" added on user model

db : Django default = SQLite

## Getting started
Clone repo and cd into directory

### Running app

```bash
docker-compose build
docker-compose up / docker-compose up -d
```

### Running migrations 
```bash
docker-compose run --rm web-app python manage.py migrate
```

### Creating super user
```bash
docker-compose run --rm web-app python manage.py migrate
```

### Running shell 
```bash
docker-compose up -d
docker-compose run --rm web-app python manage.py migrate
```

### changing Author
You will see that Author comes up as Mokgadi Rasekgala when you run the app. Change it the docker-compose.yml file to your name  or by running
```shell
docker-compose run -e AUTHOR=Lebo web-app
```
