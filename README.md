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
<details>
<Summary>Latest Updates</Summary>

Day 1
- Created Django Project "vinyl_collection"
- Created Django app "records"
- Started README.md file
- Added app to settings.py INSTALLED_APPS
- Created urls.py in records app
- Added app urls path to project urls path

Day 2
- Created Record Model
- Registered Record Model in admin.py
- Created Record ListView and CreateView
- Added ListView and CreateView url paths
- Converted Numbers. CSV file into JSON and loaded the table into SQLite database

Day 3
- Created list.html detail.html file and add.html file
- Built basic List template
- Created RecordDetailView
- Added RecordDetailView to urls.py
- Added ListView to project URL's as 'home'

Day 4
- Created css static files
- Linked static file to base.html
- Loaded Static in base.html
- Added STATICFILE_DIRS = [BASE_DIR / "static"] to project settings to point django to static file directory
- Changed BG color and text color

Day 5
- Filled in artwork data for database
- Dumped data into db.json file
---
- Added css to start styling the templates
- Created Add record template
- Created forms.py and added Record form

Day 6
- Position elements via CSS
- Stylized form in add.html using CSS
- fixed small CSS issues

Day 7
- Built Artist Model
- Edited Record Model
- Made Migrations
- Built Artist CreateView
- Built Artist Form and corresponding New Artist Template
- Connected views via urls
- Styled New Record Template
- Cleared data from tables

Day 8
- Built ArtistRecordsDetailView utilizing foreign key and context data to access wanted information
- Built artist records template utilizing context data
- Shows all Records of related artist

- CSS edits to style artist records template

- Built Search list view works for albums only for now
- Created Search results template
- Added Search form to base template

- Updated SearchView to search for Artists or Albums

- Built Edit View
- Created/Styled Edit Template
- Added EditView to URLs
- Built Delete View
- Created/Styled Delete Template
- Added DeleteView to URLs

- Styled search bar

Day 9
- Edit Page Titles

- Added links to Search Results Page

- Worked on Templates
- Edit Records List View to order data by Artist/ Date
- Edit Artist Records View to order by date
- Add artist link to record detail page
- Change all a tags to no styling and hover transition
- Small html text alterations

- Update page styling
- Search Results ordered by artist / date

- Built Signup and Profile View
- Built Signup and Profile Form
- Added owner field to Record model
- Added login, logout, signup, and profile urls to Project URLs
- Created and Styled signup, login, and profile templates

Day 10
- Updated Artist Model to display artists in order by name, and not id
- Updated List View to display only records for logged in user
- Fixed Pagination numbers (now accurately displays the users total pages of records) using get_queryset_data

</details>

### Future Updates:
- Make records only visible to owner

## Created By:

|Name|Email|GitHub|
|----|-----|-------|
|David "Lewey" Melchor|dlmelchor12@gmail.com|https://github.com/leweymelchor|
