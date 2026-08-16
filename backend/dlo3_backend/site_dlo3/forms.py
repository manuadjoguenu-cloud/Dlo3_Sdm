from django import forms
from .models import Candidature, MessageContact


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ["nom", "telephone", "paroisse", "age", "message"]
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "Votre nom complet"}),
            "telephone": forms.TextInput(attrs={"placeholder": "+228 ..."}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Un mot de motivation (facultatif)"}),
        }


class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ["nom", "email", "telephone", "sujet", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }
