from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("apropos/", views.apropos, name="apropos"),
    path("paroisses/", views.paroisses, name="paroisses"),
    path("activites/", views.activites, name="activites"),
    path("galerie/", views.galerie, name="galerie"),
    path("contact/", views.contact, name="contact"),
    #path("rejoindre/", views.rejoindre, name="rejoindre"),
    path("don/", views.don, name="don"),
    path("actualites/", views.actualites, name="actualites"),
]

