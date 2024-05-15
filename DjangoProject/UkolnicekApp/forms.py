# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:57:26 2024

@author: msi pc
"""

from django import forms
from .models import Uzivatel, Ukol, Projekt

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Uzivatel 
        exclude = ["role", "datum_vytvoreni", "posledni_zmena", "posledni_login", "prihlasen"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Uzivatel 
        fields = ["uzivatelske_jmeno", "heslo"]
        
class UserProjectForm(forms.ModelForm):
    class Meta:
        model = Uzivatel
        fields = ["uzivatelske_jmeno"]
        
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Ukol
        fields = ["nazev", "popis", "priorita"]

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ["typ_projektu"]