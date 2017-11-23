from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Tourist(models.Model):
	full_name = models.CharField(max_length=100)


class ServiceProviders(models.Model):
	full_name = models.CharField(max_length=100)
