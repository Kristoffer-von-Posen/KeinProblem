from django.db import models

# Create your models here.

# slowka


class Btwo(models.Model):
  deu = models.CharField(max_length=2048)
  qnu = models.IntegerField(blank=True, null=True)
  day = models.IntegerField(blank=True, null=True)
  week = models.IntegerField(blank=True, null=True)
  bed = models.CharField(max_length=2048, blank=True, null=True)
  art = models.IntegerField(blank=True, null=True)
  dif = models.IntegerField(blank=True, null=True)
  typ = models.CharField(max_length=2048, blank=True, null=True)

  def __str__(self):
    return f"{self.deu}"
