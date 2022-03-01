from django.contrib import admin
from .models import BookIssue

class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('issueId', 'title', 'student', 'is_closed')

admin.site.register(BookIssue, BookIssueAdmin)
