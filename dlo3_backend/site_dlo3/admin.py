from django.contrib import admin
from .models import Communaute, Activite, Photo, Don, MessageContact, Actualite


@admin.register(Communaute)
class CommunauteAdmin(admin.ModelAdmin):
    list_display = ("vocable", "lieu", "type", "responsable_spirituel", "responsable_nom", "responsable_tel")
    list_filter = ("type",)
    search_fields = ("vocable", "lieu")
    prepopulated_fields = {"slug": ("lieu",)}
    fieldsets = (
        (None, {"fields": ("slug", "type", "vocable", "lieu")}),
        ("Responsable spirituel", {"fields": ("cure", "recteur")}),
        ("Responsable de base", {"fields": ("responsable_nom", "responsable_tel")}),
        ("Localisation", {"fields": ("localisation", "carte_url", "latitude", "longitude")}),
    )


@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ("titre", "icone", "ordre")
    prepopulated_fields = {"slug": ("titre",)}
    ordering = ("ordre",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("categorie", "legende", "date_ajout")
    list_filter = ("categorie",)


@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ("nom", "montant", "moyen_paiement", "telephone", "date_envoi", "confirme")
    list_filter = ("confirme", "moyen_paiement", "paroisse")
    list_editable = ("confirme",)
    search_fields = ("nom", "telephone")

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "sujet", "date_envoi", "traite")
    list_filter = ("traite",)
    list_editable = ("traite",)
    search_fields = ("nom", "email", "message")
    
@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ("titre", "date_publication")
    date_hierarchy = "date_publication"
