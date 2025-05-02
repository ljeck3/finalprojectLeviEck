'''
INF601 - Advanced Programming in Python
Assignment: Mini Project 4
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 4

from django.urls import path

from . import views

app_name = 'wishlist'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:gift_id>/", views.detail, name="detail"),
    path("<int:gift_id>/vote/", views.respond, name="respond"),
    path("<int:gift_id>/results/", views.results, name="results")
]

