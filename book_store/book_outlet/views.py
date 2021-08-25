from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.


def index(request):
    return render(request, "book_outlet/index.html", {
        "books": Book.objects.all()
    })


def book_detail(request, id: int):
    book = get_object_or_404(Book, pk=id)
    
    return render(request, "book_outlet/book_detail.html", {
        "book": book
    })
