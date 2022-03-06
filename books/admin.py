from django.contrib import admin
from .models import Publisher, Book

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'semister', 'amount')

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
