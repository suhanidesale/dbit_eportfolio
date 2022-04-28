from django.forms import ModelForm
from .models import Internship, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title' ,'featured_image', 'description' , 'demo_link' , 'source_link','tags']

class internshipForm(ModelForm):
    class Meta:
        model = Internship
        fields = ['title' ,'featured_image', 'description' , 'source_link','tags']