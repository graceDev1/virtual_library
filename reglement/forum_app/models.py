from django.db import models
import datetime as dt 

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)


class Txtreglement(models.Model):
    text_regl = models.CharField(max_length=255)
    pdf_file = models.FileField(blank=True)


class Theme(models.Model):
    libelle = models.CharField(max_length=255)
    id_regl = models.ForeignKey(Txtreglement,on_delete=models.CASCADE)


class Message(models.Model):
    comment = models.TextField(max_length=None)
    date_comment = models.DateTimeField(auto_now_add=True)
    id_theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)



