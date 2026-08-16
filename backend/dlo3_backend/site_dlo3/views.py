import json

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Communaute, Activite, Photo
from .forms import CandidatureForm, MessageContactForm


def accueil(request):
    return render(request, "site_dlo3/accueil.html", {"page_active": "accueil"})


def apropos(request):
    contexte = {
        "page_active": "apropos",
        "total_communautes": Communaute.objects.count(),
        "total_paroisses": Communaute.objects.filter(type=Communaute.Type.PAROISSE).count(),
        "total_quasi_paroisses": Communaute.objects.filter(type=Communaute.Type.QUASI_PAROISSE).count(),
        "total_stations": Communaute.objects.filter(type=Communaute.Type.STATION).count(),
    }
    return render(request, "site_dlo3/apropos.html", contexte)


def paroisses(request):
    communautes = []
    for c in Communaute.objects.all():
        communautes.append({
            "id": c.slug,
            "type": c.type,
            "vocable": c.vocable,
            "lieu": c.lieu,
            "cure": c.cure,
            "recteur": c.recteur,
            "responsable": {"nom": c.responsable_nom, "tel": c.responsable_tel},
            "localisation": c.localisation or f"{c.lieu}, Lomé, Togo",
            "carte": c.carte_url,
            "lat": c.latitude,
            "lng": c.longitude,
        })
    contexte = {
        "page_active": "paroisses",
        "communautes_data": communautes,
        "total": len(communautes),
    }
    return render(request, "site_dlo3/paroisses.html", contexte)


def activites(request):
    liste = Activite.objects.all()
    activites_data = [
        {"id": a.slug, "icone": a.icone, "titre": a.titre, "description": a.description}
        for a in liste
    ]
    contexte = {
        "page_active": "activites",
        "activites": liste,
        "activites_data": activites_data,
        "total": liste.count(),
    }
    return render(request, "site_dlo3/activites.html", contexte)


def galerie(request):
    photos = []
    categories = set()
    for p in Photo.objects.all():
        categories.add(p.categorie)
        photos.append({
            "id": p.pk,
            "categorie": p.categorie,
            "legende": p.legende or "Légende à ajouter",
            "src": p.image.url if p.image else "",
        })
    liste_categories = ["Toutes"] + sorted(categories)
    contexte = {
        "page_active": "galerie",
        "photos_data": photos,
        "categories_data": liste_categories,
        "total": len(photos),
    }
    return render(request, "site_dlo3/galerie.html", contexte)


def contact(request):
    if request.method == "POST":
        form = MessageContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a bien été envoyé. Merci, nous reviendrons vers vous rapidement.")
            return redirect("contact")
    else:
        form = MessageContactForm()
    return render(request, "site_dlo3/contact.html", {"page_active": "contact", "form": form})


def rejoindre(request):
    if request.method == "POST":
        form = CandidatureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre candidature a bien été envoyée. Un responsable vous recontactera bientôt.")
            return redirect("rejoindre")
    else:
        form = CandidatureForm()
    return render(request, "site_dlo3/rejoindre.html", {"page_active": "rejoindre", "form": form})
