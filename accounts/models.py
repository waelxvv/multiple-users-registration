from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_condidat = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Telephone = models.IntegerField(null=True, blank=True)
    Adresse = models.CharField(max_length=30, blank=True)
    DateDeNaissance = models.DateField(null=True, blank=True)
    SalaireSouhaite = models.FloatField(null=True, blank=True)
    Motivation = models.CharField(max_length=150, blank=True)
    DateDeDisponibilite = models.DateField(null=True, blank=True)
    Reponse = models.CharField(max_length=30, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Telephone = models.IntegerField(null=True, blank=True)
    Adresse = models.CharField(max_length=30, blank=True)
    DateDeNaissance = models.DateField(null=True, blank=True)
    PosteActuelle = models.CharField(max_length=30, blank=True)
    DateRecrutement = models.DateField(null=True, blank=True)
    DateOccupationPosteActuelle = models.DateField(null=True, blank=True)
    Directeur = models.CharField(max_length=30, blank=True)
    SoldeConge = models.FloatField(null=True, blank=True)
    NbrDeJourCongeParMois = models.FloatField(null=True, blank=True)
