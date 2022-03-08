from django.db import models
from uuid import uuid4
from django.utils.text import slugify
from students.models import Student
from librarians.models import Librarian
from books.models import Book


class BookIssue(models.Model):
    issueId = models.CharField(max_length=50, null=True, blank=True, editable=False)
    title = models.CharField(max_length=100, default='Book reception info')
    slug = models.CharField(max_length=200, null=True, blank=True)

    # Related Fields
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    # Utility Fields
    issue_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    is_closed = models.BooleanField(default=False)

    def close_issue(self):
        """
        This method will close a opened book issue
        """
        self.is_closed = True

    class Meta:
        verbose_name_plural = 'bookissues'

    def __str__(self):
        return f'{self.title} - {self.issueId} - {self.student.name}'

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.title)
        if self.issueId == None:
            unique_data = str(uuid4()).split('-')[4][:5]
            self.issueId = slugify('BI-{}-{}.{}'.format(unique_data, self.student.department.name, self.student.semister))
        super(BookIssue, self).save(*args, **kwargs)
