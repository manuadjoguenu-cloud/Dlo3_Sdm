from django import forms
from .models import Don, MessageContact


class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ["nom", "telephone", "montant", "moyen_paiement", "paroisse", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 3, "placeholder": "Un mot (facultatif)"}),
        }


class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ["nom", "email", "telephone", "sujet", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }
