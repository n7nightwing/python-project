## Python Project
- [Mockups](https://xd.adobe.com/view/c03d03f3-5841-473b-4f38-242ef961504a-b60c/)

## Movies and directors!

The purpose of this app is to show off our favorite movies and the brilliant minds behind them! Featured will be movies with brief details about them, and they will all be associated with the directors who made them possible!

## Installation and getting started
1. fork and clone this repository.
2. initialize the virtualenv (source .env/bin/activate)
3. make sure django is installed (pip install django)
4. create database with name (movieworld), and a user that has access to that database.
5. Update settings.py with database information.
6. Run migrations "python manage.py migrate"
7. Happy coding!

## Models

### Movie:
Fields:
- 'name'
- 'genre'
- 'release_date'
- 'director_name' - foreignkey
- 'synopsis'
- 'photo_url'

### Director:
Fields:
- 'name'
- 'nationality'
- 'birthday'
- 'bio'
- 'movies' - foreignkey
- 'photo_url'

## Completed Tasks:
- Define a model
- migrate

- add database to settings in movieworld_django
- create superuser/admin
- create a view
- create urls
- create HTML templates
- Create
- Read
- Update
- Delete 

KF:
1. created forms.py
2. added movie_create in views.py
3. added director_create in views.py
4. added movie_edit in views.py
5. added director_edit in views.py
6. added movie_delete in views.py
7. added director_delete in views.py
8. created templates folder:
- base.html
- movie_list.html
- director_list.html 
- movie_detail.html
- director_detail.html
- movie_form.html
- director_form.html
9. CSS: movieworld/static/css/movieworld.css
10. added paths to movieworld/urls.py

## Loose ends ..
- movie details needs details
- directordetails page is blank
- styling
- no delete functions
