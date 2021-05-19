from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookList),
    path('authors', views.authorList),
    path('add_book', views.addBook),
    path('add_author', views.addAuthor),
    path('assignAuthorToBook', views.assignAuthorToBook),
    path('assignBookToAuthor', views.assignBookToAuthor),
    path('books/<int:id_num>', views.bookPage),
    path('authors/<int:id_num>', views.authorPage),
]