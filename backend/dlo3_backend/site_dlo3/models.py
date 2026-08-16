from django.db import models


class Communaute(models.Model):
    """Une paroisse, quasi-paroisse, station secondaire ou sanctuaire du doyenné."""

    class Type(models.TextChoices):
        PAROISSE = "Paroisse", "Paroisse"
        QUASI_PAROISSE = "Quasi-Paroisse", "Quasi-Paroisse"
        STATION = "Station secondaire", "Station secondaire"
        SANCTUAIRE = "Sanctuaire", "Sanctuaire"

    slug = models.SlugField(unique=True, help_text="Identifiant technique, ex. « adidogome »")
    type = models.CharField(max_length=30, choices=Type.choices)
    vocable = models.CharField(max_length=150, help_text="Ex. « Marie Mère du Rédempteur »")
    lieu = models.CharField(max_length=100)

    # Curé (paroisses/quasi-paroisses/stations) ou recteur (sanctuaire) — un seul des deux est rempli.
    cure = models.CharField(max_length=150, blank=True)
    recteur = models.CharField(max_length=150, blank=True)

    responsable_nom = models.CharField(max_length=150, blank=True)
    responsable_tel = models.CharField(max_length=30, blank=True)

    localisation = models.CharField(max_length=255, blank=True, help_text="Texte libre affiché dans la fiche")
    carte_url = models.URLField(blank=True, help_text="Lien de partage Google Maps précis (facultatif)")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Communauté"
        verbose_name_plural = "Communautés"
        ordering = ["type", "vocable"]

    def __str__(self):
        return f"{self.vocable} — {self.lieu}"

    @property
    def responsable_spirituel(self):
        """Le nom à afficher dans la fiche, avec le bon libellé (Curé/Recteur)."""
        if self.type == self.Type.SANCTUAIRE:
            return self.recteur or "À renseigner"
        return self.cure or "À renseigner"

    @property
    def label_responsable_spirituel(self):
        return "Recteur" if self.type == self.Type.SANCTUAIRE else "Curé"


class Activite(models.Model):
    """Une des cartes de la page Activités (Réunion, Récollection, Camp, Journée d'amitié...)."""

    slug = models.SlugField(unique=True)
    icone = models.CharField(max_length=10, help_text="Emoji, ex. 🤝")
    titre = models.CharField(max_length=150)
    accroche = models.CharField(max_length=150, blank=True, help_text="Phrase courte visible sur la carte")
    description = models.TextField(blank=True)
    fichier = models.FileField(upload_to="activites/", blank=True, null=True,
                                help_text="Programme au format PDF ou Word (facultatif)")
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Activité"
        verbose_name_plural = "Activités"
        ordering = ["ordre", "titre"]

    def __str__(self):
        return self.titre


class Photo(models.Model):
    """Une photo de la galerie."""

    categorie = models.CharField(max_length=100)
    legende = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="galerie/")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ["-date_ajout"]

    def __str__(self):
        return f"{self.categorie} — {self.legende or 'sans légende'}"


class Candidature(models.Model):
    """Formulaire « Rejoindre les servants »."""

    nom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=30)
    paroisse = models.ForeignKey(Communaute, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name="candidatures")
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    message = models.TextField(blank=True)
    date_envoi = models.DateTimeField(auto_now_add=True)
    traitee = models.BooleanField(default=False, help_text="Cochée une fois le candidat recontacté")

    class Meta:
        verbose_name = "Candidature"
        verbose_name_plural = "Candidatures (Rejoindre les servants)"
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.nom} ({self.date_envoi:%d/%m/%Y})"


class MessageContact(models.Model):
    """Formulaire de la page Contact."""

    nom = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    sujet = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.nom} — {self.sujet or 'sans sujet'}"
