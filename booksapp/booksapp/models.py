from django.db import models
from django.http import QueryDict
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

class Author(models.Model): 
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	pseudonym = models.CharField(max_length=20)
	age = models.IntegerField()

	def __str__(self):
		return self.pseudonym


class Company(models.Model):
	company_name = models.CharField(max_length=50)

	def __str__(self):
		return self.company_name


class Book(models.Model):
	name = models.CharField(max_length=50)
	publish_year = models.IntegerField()
	genre = models.CharField(max_length=20)
	publish_company = models.ForeignKey(Company)
	author = models.ForeignKey(Author)
