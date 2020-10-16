from django.conf import settings
from django.db import models
from django.utils import timezone

class Grundwasserstand(models.Model):
    messdat = models.DateTimeField()
    gwh = models.FloatField()
    gwt = models.FloatField()
    bnr = models.IntegerField()
# messdat:"07.01.1900 12:00",
# gwh:28.89,
# gwt:null,
# bnr:"00005"
# gwh: Grundwasserhöhe
# messdat: Datum und Uhrzeit der Messung
# gwt: Grundwassertemperatur
# bnr: Brunnennummer / Nummer der Messstelle
