from django.urls import path

from . import views

app_name = 'guestbook'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:memo_id>/", views.detail, name="detail"),
    path('compose/', views.compose, name='compose'),

]