# Vinyl Collection

## Description
A place to store your record collection and keep additional data about each record

## Project Goals
I plan to use my knowledge of Django, Python, HTML, and CSS to build this project.
The main goal is to build User sign up page, a user profile page that links to each users collection of records,
a login and logout functionality, the ability to add name, album title, album cover art, album date released, and price, then i also want to display the total cost of the collection.
Building a carousel view for the collection would be nice, but a paginated list may be better to sort the information by different filters, whichever works best. Then I want the overall user experience to be a beutiful one that is easy to use. I will focus on code cleanliness and code reusability

## Start it up
- Clone this repository into a fresh directory on your computer
- Create a virtual environment. Make sure you are in the freshly cloned folder when you do this!
    - `python -m venv .venv`
- Activate the virtual enviornment.
    - `source .venv/bin/activate`
- Install the required packages.
    - `pip install -r requirements.txt`
- Run migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- Create a super user
    - `python manage.py createsuperuser`
    - follow terminal prompts
- Install recipes
    - `python manage.py loaddata db.json`
- Run server
    - `python manage.py runserver`
- Open your browser to http://localhost:8000
- ENJOY!!!

### Latest Updates:
- Created Django Project "vinyl_collection"
- Created Django app "records"
- Started README.md file

### Future Updates:

## Created By:

|Name|Email|GitHub|
|----|-----|-------|
|David "Lewey" Melchor|dlmelchor12@gmail.com|https://github.com/leweymelchor|
