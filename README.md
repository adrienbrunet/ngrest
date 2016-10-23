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

------------------------------------------------------------------
Creators: Xavier Ordoquy [@xordoquy](https://github.com/xordoquy) and Adrien Brunet [@adrienbrunet](https://github.com/adrienbrunet)
