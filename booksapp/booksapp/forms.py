from django import forms
from .models import Author, Company, Book

class AuthorForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    pseudonym = forms.CharField(label="Pseudonym", max_length=30)
    age = forms.IntegerField(label="age")

    class Meta:
	    model = Author
	    fields = ['first_name', 'last_name', 'pseudonym', 'age']


class CompanyForm(forms.ModelForm):
	company_name = forms.CharField(label="company_name", max_length=50)

	class Meta:
		model = Company
		fields = ['company_name']


class BookForm(forms.ModelForm):
	name = forms.CharField(label="name", max_length=50)
	publish_year = forms.IntegerField(label="publish_year")
	genre = forms.CharField(label="genre", max_length=50)
	publish_company = forms.ModelChoiceField(queryset=Company.objects.all())
	author = forms.ModelChoiceField(queryset=Author.objects.all())

	class Meta:
		model = Book
		fields = ['name', 'publish_year', 'genre', 'publish_company', 'author']

