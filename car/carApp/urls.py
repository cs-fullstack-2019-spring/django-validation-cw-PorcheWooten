from django.urls import path
from . import views

# the superuser admin is admin password = test4321
urlpatterns = \
    [
        path('',views.index, name ='index'),
        path('congrats/',views.congrats, name ='congrats'),
    ]