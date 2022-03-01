from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField(max_length=600)

    class Meta:
        verbose_name_plural = 'departments'

    def __str__(self):
        return f'{self.name} - {self.code}'


class Student(models.Model):
    semisters = (
        ('1','1st'),
        ('2','2nd'),
        ('3','3rd'),
        ('4','4th'),
        ('5','5th'),
        ('6','6th'),
        ('7','7th'),
        ('8','8th'),
    )
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    stdId = models.CharField(max_length=50, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semister = models.CharField(choices=semisters, max_length=50)
    dob = models.DateField()
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    religion = models.CharField(max_length=100)
    gender = models.CharField(choices=gender, max_length=100)

    class Meta:
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.stdId} - {self.name}'

    def save(self, *args, **kwargs):
        if self.stdId == None:
            if self.name[4] != ' ':
                i = 4
            else:
                i = 5
            self.stdId = self.name[i]+str(self.department.code)+self.department.name
            print('self.stdId : ', self.stdId)
        super(Student, self).save(*args, **kwargs)
"""
If need then we can use, 
# uniqueId = str(uuid.uuid4()).split('-')[4]
# self.stdId = slugify('{} {} {}'.format(self.name, uniqueId, self.department))
"""
