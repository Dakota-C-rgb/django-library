from django.contrib import admin
from app.models import Book, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
