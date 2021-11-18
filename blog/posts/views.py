from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post, Author
# Create your views here.
def index(request):
    return render(request, "posts/index.html", {
        "posts": Post.objects.all()
    })

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    authors = post.authors.all()
    return render(request, "posts/post_detail.html", {
        "post": post,
        "authors": authors,
        # "non_authors": Author.objects.exclude(posts=post).all(),
    })

""" def book(request, flight_id):

    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,))) """