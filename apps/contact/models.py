from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    message = models.TextField()
    consent = models.BooleanField()

    def __str__(self):
        return self.email
