

from django.db import models

class mydata(models.Model):
    end_year=models.IntegerField(unique=False,blank=True)
    intensity=models.CharField(unique=False,max_length=1000,blank=True)
    sector = models.CharField(unique=False,max_length=1000, blank=True)
    topic = models.CharField(max_length=1000,unique=False, blank=True)
    insight = models.CharField(max_length=1000, blank=True,unique=False)
    url = models.CharField(max_length=1000,unique=False, blank=True)
    region = models.CharField(max_length=1000,unique=False, blank=True)
    start_year=models.IntegerField(blank=True,unique=False)
    impact = models.CharField(max_length=1000, unique=False,blank=True)
    added= models.CharField(max_length=1000,unique=False, blank=True)
    published= models.CharField(max_length=1000,unique=False, blank=True)
    country = models.CharField(max_length=1000,unique=False, blank=True)
    relevance=models.IntegerField(blank=True,unique=False)
    pestle = models.CharField(max_length=1000,unique=False, blank=True)
    source = models.CharField(max_length=1000,unique=False, blank=True)
    title = models.CharField(max_length=1000,unique=False, blank=True)
    likelihood = models.IntegerField(blank=True,unique=False)


