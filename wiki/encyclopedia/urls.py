from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entryName>", views.entry, name="entry"),
    path("random", views.random, name="random"),
    path("search", views.search, name='search'),
    path("createPage", views.createPage, name="createPage"),
    path("wiki/editPage/<str:entryName>", views.editPage, name="editPage"),
    path("postEdit", views.postEdit, name = "postEdit")
]
