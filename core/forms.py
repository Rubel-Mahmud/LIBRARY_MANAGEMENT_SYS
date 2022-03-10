from django import forms
from students.models import Student

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob':DateInput(),
            'address':forms.Textarea(attrs={'rows':6})
        }
