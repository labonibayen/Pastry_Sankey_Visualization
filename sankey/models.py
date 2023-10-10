from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import admin

########## DEFINE MODELS #############################

class DataPoint(models.Model):
	
	id = models.AutoField(primary_key=True)
	pastry = models.CharField(max_length=200, default='SOME STRING')
	base = models.CharField(max_length=500, default='SOME STRING')
	origin = models.CharField(max_length=200)
	pastry_description = models.CharField(max_length=1000, default=True)
	base_description = models.CharField(max_length=5000, default=True)
	in_sankey = models.BooleanField(default=False)
	rank = models.IntegerField(default=0)

	class Meta:
		ordering = ('rank',)
	

	def __str__(self):
		return self.pastry
