from django.db import models

class Librarian(models.Model):
    libId = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    photo = models.ImageField(max_length=600)

    class Meta:
        verbose_name_plural = 'librarians'

    def __str__(self):
        return self.name
