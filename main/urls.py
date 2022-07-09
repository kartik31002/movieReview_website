#this is our main app , we create apps in our website which are of two types one is main app(i.e this) and one is accounts app

from django.urls import path
from . import views
app_name ="main"

urlpatterns = [
    path('',views.home, name="home"), #here blank sapce in first ' ' because it is supposed to be our home page. there is nothing before to be written before the url of our home page
    path('details/<int:id>/' , views.detail, name="detail"),
    path('search/' , views.searchresults, name="searchresults"),
]
