from django.forms import ModelForm, BooleanField
from django.forms.widgets import Textarea, TextInput
from django.utils.translation import gettext_lazy as _

from .models import Contact


class ContactForm(ModelForm):
    consent = BooleanField(required=True)

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message", "consent"]
        help_texts = {
            "name": _("Write your name here"),
            "email": _("Write your email here"),
            "phone_number": _("Write your telephone number here"),
            "message": _("Tell us how we can help you"),
        }
        widgets = {
            "message": Textarea(attrs={"rows": 10, "class": "textarea"}),
            "name": TextInput(attrs={"class": "input"}),
            "email": TextInput(attrs={"class": "input"}),
            "phone_number": TextInput(attrs={"class": "input"}),
        }
