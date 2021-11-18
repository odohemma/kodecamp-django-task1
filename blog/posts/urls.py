from django.urls import path

from . import views

# app_name = "flights" #"flights" refers to the template/tasks directory

urlpatterns = [
    path ("", views.index, name="index"),
    path("<int:post_id>", views.post, name="post"),
]