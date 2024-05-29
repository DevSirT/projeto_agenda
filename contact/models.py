from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=9999, blank=True)
