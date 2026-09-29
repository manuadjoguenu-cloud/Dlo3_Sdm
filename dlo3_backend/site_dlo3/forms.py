from django import forms
from django.core.cache import cache

from .models import Don, MessageContact

MONTANT_MAX = 5_000_000  # FCFA


class AntiSpamMixin:
    """Champ piège (honeypot) invisible pour les humains + limitation par IP."""

    limite_par_heure = 5
    prefixe_cache = "form"

    def __init__(self, *args, request=None, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        self.fields["site_web"] = forms.CharField(
            required=False,
            label="",
            widget=forms.TextInput(attrs={
                "tabindex": "-1", "autocomplete": "off",
                "style": "position:absolute;left:-9999px;", "aria-hidden": "true",
            }),
        )

    def _ip(self):
        if not self.request:
            return "inconnue"
        return self.request.META.get("REMOTE_ADDR", "inconnue")

    def clean(self):
        data = super().clean()
        if data.get("site_web"):
            raise forms.ValidationError("Envoi refusé.")
        cle = f"{self.prefixe_cache}:{self._ip()}"
        if cache.get(cle, 0) >= self.limite_par_heure:
            raise forms.ValidationError("Trop d'envois. Réessayez dans une heure.")
        return data

    def enregistrer_tentative(self):
        cle = f"{self.prefixe_cache}:{self._ip()}"
        cache.set(cle, cache.get(cle, 0) + 1, 3600)


class DonForm(AntiSpamMixin, forms.ModelForm):
    prefixe_cache = "don"

    class Meta:
        model = Don
        fields = ["nom", "telephone", "montant", "moyen_paiement", "paroisse", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 3, "placeholder": "Un mot (facultatif)"}),
        }

    def clean_montant(self):
        montant = self.cleaned_data["montant"]
        if montant < 100 or montant > MONTANT_MAX:
            raise forms.ValidationError(f"Le montant doit être entre 100 et {MONTANT_MAX:,} FCFA.".replace(",", " "))
        return montant


class MessageContactForm(AntiSpamMixin, forms.ModelForm):
    prefixe_cache = "contact"

    class Meta:
        model = MessageContact
        fields = ["nom", "email", "telephone", "sujet", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }
