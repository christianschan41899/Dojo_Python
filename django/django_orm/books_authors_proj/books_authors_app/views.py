from django.shortcuts import render, redirect
from .models import Book, Author

#Main page listing all books and can add books from
def bookList(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, 'mainBookPage.html', context)

#Main page listing all authors and can add authors from
def authorList(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, 'mainAuthorPage.html', context)

#Processes the request to add books
def addBook(request):
    Book.objects.create(title = request.POST["input_title"], desc = request.POST["input_desc"])
    return redirect('/')

def addAuthor(request):
    Author.objects.create(first_name = request.POST["input_fName"], last_name = request.POST["input_lName"], notes = request.POST["input_notes"])
    return redirect('/authors')

#Renders the book and it's information, as well as passes authors if we need to add an author.
def bookPage(request, id_num):
    context = {
        "this_book" : Book.objects.get(id=id_num),
        "authors" : Author.objects.all()
    }
    return render(request, "individualBookPage.html", context)

#Renders page that displays individual information of an author, as well as letting you to choose a book to add to an author
def authorPage(request, id_num):
    context = {
        "this_author" : Author.objects.get(id=id_num),
        "books" : Book.objects.all()
    }
    return render(request, "individualAuthorPage.html", context)

#Adds an author to a book's ManyToManyField
def assignAuthorToBook(request):
    returnPath = request.POST['returnTo']
    postAuthorID = request.POST['author']
    bookID = request.POST['bookID']
    current_book = Book.objects.get(id = bookID)
    current_book.authors.add(Author.objects.get(id = postAuthorID))
    current_book.save()
    return redirect(returnPath)

#Adds a book to an author's ManyToManyField
def assignBookToAuthor(request):
    returnPath = request.POST['returnTo']
    postBookID = request.POST['book']
    authorID = request.POST['authorID']
    current_author = Author.objects.get(id = authorID)
    current_author.books.add(Book.objects.get(id = postBookID))
    current_author.save()
    return redirect(returnPath)
