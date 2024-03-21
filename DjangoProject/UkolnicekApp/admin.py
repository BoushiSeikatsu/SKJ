from django.contrib import admin
from .models import Role, StavUkolu, TypProjektu, Uzivatel, Projekt, Ukol, HistorieUzivatelu, Pratelstvi, UzivatelProjekt
# Register your models here.

admin.site.register(Role)
admin.site.register(StavUkolu)
admin.site.register(TypProjektu)
admin.site.register(Uzivatel)
admin.site.register(Projekt)
admin.site.register(Ukol)
admin.site.register(HistorieUzivatelu)
admin.site.register(Pratelstvi)
admin.site.register(UzivatelProjekt)