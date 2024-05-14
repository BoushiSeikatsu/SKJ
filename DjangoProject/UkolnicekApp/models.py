from django.db import models

# Create your models here.
from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=25, null=False)
    privilegie = models.CharField(max_length=255, null=False)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nazev

class StavUkolu(models.Model):
    stav_ukolu_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=25, null=False)
    popis = models.CharField(max_length=255, null=False)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nazev

class TypProjektu(models.Model):
    typ_projektu_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=25, null=False)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nazev

class Uzivatel(models.Model):
    uzivatel_id = models.AutoField(primary_key=True)
    uzivatelske_jmeno = models.CharField(max_length=25, null=False)
    krestni_jmeno = models.CharField(max_length=25, null=False)
    prijmeni = models.CharField(max_length=25, null=False)
    heslo = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=50, null=False)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True, null=True)
    posledni_login = models.DateTimeField(blank=True, null=True)
    prihlasen = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.uzivatelske_jmeno}, {self.role.nazev}'

class Projekt(models.Model):
    projekt_id = models.AutoField(primary_key=True)
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING)
    typ_projektu = models.ForeignKey(TypProjektu, on_delete=models.DO_NOTHING)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.projekt_id} {self.typ_projektu.nazev}"  # You can customize the display name here

class Ukol(models.Model):
    ukol_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=25, null=False)
    popis = models.CharField(max_length=255, null=False)
    priorita = models.IntegerField(null=False)
    stav_ukolu = models.ForeignKey(StavUkolu, on_delete=models.DO_NOTHING)
    nejzazsi_termin = models.DateTimeField(null=False)
    projekt = models.ForeignKey(Projekt, on_delete=models.DO_NOTHING)
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING, blank=True, null=True)
    datum_vybrani = models.DateTimeField(blank=True, null=True)
    datum_dokonceni = models.DateTimeField(blank=True, null=True)
    predpo_cas = models.IntegerField(null=False)
    datum_vytvoreni = models.DateTimeField(null=False)
    posledni_zmena = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.nazev

class HistorieUzivatelu(models.Model):
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING)
    projekt = models.ForeignKey(Projekt, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uzivatel', 'projekt'], name='Historie_uzivatelu_PK'),
        ]

    def __str__(self):
        return f"{self.uzivatel} - {self.projekt}"

class Pratelstvi(models.Model):
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING, related_name='following')
    pritel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING, related_name='followers')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uzivatel', 'pritel'], name='Pratelstvi_PK'),
        ]

    def __str__(self):
        return f"{self.uzivatel.uzivatelske_jmeno} follows {self.pritel.uzivatelske_jmeno}"

class UzivatelProjekt(models.Model):
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.DO_NOTHING)
    projekt = models.ForeignKey(Projekt, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uzivatel', 'projekt'], name='Uzivatel_Projektv1_PK'),
        ]

    def __str__(self):
        return f"{self.uzivatel.uzivatelske_jmeno} - {self.projekt.projekt_id}"