<!--
INF601 - Advanced Programming in Python
Assignment: Final Project
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
-->

### INF601 - Advanced Programming in Python
### Levi Eck
### Final Project


# Django Wedding Website



## Description

This project uses Django to provide many features that would appear on a wedding website. This includes the ability to RSVP, view and write on an electronic guestbook, and view the registry. It also builds upon some work from my Miniproject 4.

## Getting Started

### Dependencies
```
pip install -r requirements.txt
```

### Executing program
If changes are made to the models, run this command first to create the SQL entries that need to go into the database:
```
python manage.py makemigrations
``````
Apply migrations (initialize the database):
```
python manage.py migrate
``````
Create a superuser (admin):
```
python manage.py createsuperuser
``````
Run the development server:
```
python manage.py runserver
``````


### Creating events and adding guests

Once server is running, go to http://127.0.0.1:8000/admin/. There is an Events tab and a Guests tab. 

## Authors

Levi Eck

## Acknowledgments

Inspiration, code snippets, etc.
* [Django](https://www.djangoproject.com/)
* [Django Polls Tutorial](https://docs.djangoproject.com/en/4.2/intro/)
* [Codemy](https://www.youtube.com/watch?v=CTrVDi3tt8o)
* [ChatGPT troubleshooting](https://chatgpt.com/share/67f340fe-65f4-8001-bab6-2d183eb4e2eb)