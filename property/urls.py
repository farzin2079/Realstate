from django.urls import path
from . import views


urlpatterns = [
    path("", views.index , name="property"),
    path("addnew", views.addprop , name="addnew"),
    path("details/<int:id>", views.details , name="details"),
    path("delete", views.delete , name="delete"),
    path("watchlist/<int:id>", views.watchlist , name="watchlist"),
    path("category/<int:id>", views.category , name="category"),
]

