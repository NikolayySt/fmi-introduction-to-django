from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Author, Company
from .forms import AuthorForm, CompanyForm, BookForm

def books(request):
	all_books = Book.objects.all()
	return render(request, 'booksapp/books.html',{
		'all_books': all_books,
	})

def create_book(request):
	if request.method == 'GET':
		companies = Company.objects.all()
		authors = Author.objects.all()
		return render(request, 'booksapp/createBook.html',{
		    'companies': companies,
		    'authors': authors
		})

	if request.method == 'POST':
		create_form = BookForm(request.POST)
		if create_form.is_valid():
			book = create_form.save(commit=False)

		return redirect('/')

def authors(request):
	all_authors = Author.objects.all()
	return render(request, 'booksapp/authors.html', {
		'all_authors': all_authors,
	})

def create_author(request):
	if request.method == 'GET':
		return render(request, 'booksapp/createAuthor.html')

	if request.method == 'POST':
		create_form = AuthorForm(request.POST)
		if create_form.is_valid():
			author = create_form.save(commit=False)
			author.save()
		
		return redirect('/authors')

def companies(request):
	all_companies = Company.objects.all()
	return render(request, 'booksapp/companies.html', {
		'all_companies': all_companies,
	})

def create_company(request):
    if request.method == 'GET':
        return render(request, 'booksapp/createCompany.html')

    if request.method == 'POST':
	    create_form = CompanyForm(request.POST)
	    if create_form.is_valid():
		    company = create_form.save(commit=False)
		    company.save()
		
	    return redirect('/companies')