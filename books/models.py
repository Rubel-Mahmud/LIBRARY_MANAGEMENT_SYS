from django.db import models
from students.models import Department

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'publishers'

    def __str__(self):
        return self.name


class Book(models.Model):
    semisters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semister = models.CharField(choices=semisters, max_length=50)
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name} - {self.publisher}'

    def book_return(self):
        """
        When any student will return book then book amount will increase one more
        Because a student can take only one book at a time.
        """
        self.amount += 1

    def book_delivery(self):
        """
        When any student will take book then book amount will decrease one more
        Because a student can take only one book at a time.
        """
        self.amount -= 1

    def is_book_available(self):
        """
        If totall amount of any book is zero then this method will return 0.
        Otherwise it will return 1.
        """
        if self.amount != 0:
            return 1
        else:
            return 0
