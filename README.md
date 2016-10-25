# ngrest

Small demo app to build forms in angular from django modelSerializers with django-rest-framework.

Right now working on angular1.x, support for angular2 is coming...

## Install

```bash
pip install -r requirements.txt
```

## Back

Launch django on 127.0.0.1:8000

```bash
cd back
./manage.py migrate
./manage.py runserver
```

## Front

Launch the angular app on 127.0.0.1:8080 using ES6 and webpack

```bash
cd front
npm install
npm start
```

## Sqlite3 limitation

With sqlite3 (by default with this repo), you may face problems with model field's validators.
Example: a `PositiveIntegerField`, after being serializer, won't have `min_value=0` as an attribute.
It's because sqlite does not enforce any limits on its fields.

You might want to use another db. To use postgres, uncomment the requirements.txt line with postgres, pip install it, setup your postgres database and update the settings.py.

------------------------------------------------------------------
Creators: Xavier Ordoquy [@xordoquy](https://github.com/xordoquy) and Adrien Brunet [@adrienbrunet](https://github.com/adrienbrunet)
