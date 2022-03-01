from django.contrib import admin
from .models import Librarian

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('libId', 'name')

admin.site.register(Librarian, LibrarianAdmin)
