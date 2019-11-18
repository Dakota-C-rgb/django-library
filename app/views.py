from django.shortcuts import render, redirect
from app.models import Book, Transaction
from django.contrib import messages
from datetime import datetime

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books":books})

def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock:
        transaction = book.transaction_set.create(date_purchased=datetime.now(), 
        action="CHECKOUT", book=book)
        messages.success(request, f"Borrowed {book.title} by {book.author}")
        book.in_stock = False
        book.save()
        return redirect("home")
    else:
        messages.error(request, f"{book.title} by {book.author} is unavailable")
        return redirect("home")
    
def return_book(request, id):
    book = Book.objects.get(id=id)
    if not book.in_stock:
        messages.success(request, f"Returned {book.title} by {book.author}")
        transaction = book.transaction_set.create(date_purchased=datetime.now(), 
        action="CHECKIN", book=book)
        book.in_stock = True
        book.save()
        return redirect("home")
    if book.in_stock:
        messages.error(request, f"{book.title} by {book.author} is already here")
        return redirect("home")
