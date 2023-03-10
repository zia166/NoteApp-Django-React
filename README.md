# Notes App
A simple Notes App made using React JS, Redux and Django Rest Framework. I was trying to connect my Django, React JS skills together, so I built this.

<br/>

<div align="center"><img src="Home Page.png" alt="base" border="0"><p>HomePage</div>


## Technologies used:

- Backend - `Django` + `Django Rest Framework`
- Frontend - `ReactJS`
- Styling - `vanilla CSS`
-`React Router` for routing (frontend)
- Database - `SQLite3`. But you can easily plug and use the DB of your choice.

## Description

This is a simple note taking app with Token Based Authentication. After that they will be able to use this Notes App. The users will be able to do the following:

- Create a note
- Delete  note


A single `note` consists of the following data:

- `title` - the title of the note
- `body` - the content of the note
- `created_at` - when it was created


## How to use it?

I developed both the Django backend and the ReactJS frontend seperately and merge it later. 
One of the many ways to run this project is to **run the Django backend API alone** and then **use the React frontend to consume the API**.

So to do that, first:

- `git clone` or `Download ZIP` this repo `https://github.com/zia166/NoteApp-Django-React.git`

Then setup the Backend...

# Backend Setup

To setup and start/activate the Backend API server, do the following:

- `cd Notes/notes/notes/`

## Setting up a virtual environment using venv
- `python -m venv venv` will make a virtual environment
- `source venv/bin/activate` to activate the venv. (If you are on windows, then run this instead `venv\Scripts\activate.bat`)

## Installing the requirements
- `pip install -r requirements.txt` will install the needed backend project requirements

## Making migrations
- `python manage.py makemigrations`
- `python manage.py migrate`

## Creating the super user
- `python manage.py createsuperuser` and provide the needed infos

## Starting the backend API server
- `python manage.py runserver` will start the Django API server

- At this point, if you want, you can **Login** to the pre-built admin panel by visiting- `http://localhost:8000/admin/` in your browser as the superuser account you just created. From this panel, you will be able to do almost anything to the applicaiton!

<br/>
Now our backend server is ready to accept the API requests! So let's setup the frontend...
<br/>

# Frontend Setup

Now let's run our frontend so that we can visually interact with our backend API.

- Open up another terminal and `cd notes/frontend/`
- `npm install` will install all the needed modules for the frontend to work
- `npm run start` to start the frontend development server
- Visit `http://localhost:3000` in your browser (normally ReactJS would do this for us)
- Login/Register and enjoy the application!

## Thanks for having a look at my project.
