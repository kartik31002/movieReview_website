#logic of our code goes here
#any pages you wanna create goes here
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from urllib import response
import requests
#function based views

apiBaseURL = 'https://api.themoviedb.org/3/'
apiKey = '3d9b4ef8cf0ea93474001f18dabe2e00'

imagebase = 'https://image.tmdb.org/t/p/w300'

#home page
def home(request): #what the users will see on our front page every view that has to be viewed i the html has to go thru request parameter
    # allMovies= Movie.objects.all() # select * from Movie (equivalent SQL query)
    # # we need to create a dictionary for our html template. Html file will contain "movies" which will refer to allMovies
    # context = {
    #     "movies" : allMovies,
    # }
    response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'main/index.html', {'response3' : response3})

#detail page
def detail(request,id):
    # movie= Movie.objects.get(id=id) #select * from Moview where id=id
    # context = {
    #     "movie" : movie
    # }
    response = requests.get(apiBaseURL + 'movie/' + str(id) + '?api_key=' + apiKey).json()
    title = response["title"]
    overview = response["overview"]
    rating = response["vote_average"]
    release = response["release_date"]
    imageurl = imagebase + response["poster_path"]
    if Movie.objects.filter(name=title).exists():
        pass
    else:
        moviedata = Movie(name=title, description=overview, averageRating=rating, release_date=release, image=imageurl)
        moviedata.save()
    # review = reviews.objects.all().filter(movieid = movie_id)
    return render(request, 'main/details.html', {'response':response})

#search a movie

def searchresults(request):
    searchTerm = request.POST.get("searchTerm")
    response = requests.get(apiBaseURL + 'search/movie?api_key=' + apiKey + '&language=en-US&page=1&include_adult=false&query=' + searchTerm).json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'main/search.html/', {'response3' : response3, 'searchTerm':searchTerm})

