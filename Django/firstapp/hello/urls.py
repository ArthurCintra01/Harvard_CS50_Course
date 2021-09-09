from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("arthur",views.arthur, name="arthur"),
    path("<str:name>", views.greet, name="greet")
]