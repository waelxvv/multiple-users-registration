from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Candidat,Employee

class CandidatSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    Telephone = forms.IntegerField(required=True)
    Adresse = forms.CharField(required=True)
    DateDeNaissance = forms.DateField(required=True)
    SalaireSouhaite = forms.FloatField(required=True)
    Motivation = forms.CharField(required=True)
    DateDeDisponibilite = forms.DateField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidat = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        candidat = Candidat.objects.create(user=user)
        candidat.Telephone=self.cleaned_data.get('Telephone')
        candidat.Adresse=self.cleaned_data.get('Adresse')
        candidat.DateDeNaissance=self.cleaned_data.get('DateDeNaissance')
        candidat.SalaireSouhaite=self.cleaned_data.get('SalaireSouhaite')
        candidat.Motivation=self.cleaned_data.get('Motivation')
        candidat.DateDeDisponibilite=self.cleaned_data.get('DateDeDisponibilite')
        candidat.save()
        return user

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.save()
        return user
