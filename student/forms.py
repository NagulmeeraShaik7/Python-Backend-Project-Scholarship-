from pyexpat import model
from django import forms 

from .models import Student 

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student 
        fields = '__all__' 
