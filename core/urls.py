from django.contrib import admin
from django.urls import path, include
from librarians.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home view
    path('', home, name='home'),
    # Students urls
    path('students/', include('students.urls')),
    # Book_issues urls
    path('issues/', include('book_issues.urls')),
    # Books urls
    path('books/', include('books.urls'))
]
