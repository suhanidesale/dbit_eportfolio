from logging import PlaceHolder
from django.forms import ModelForm
from matplotlib import widgets
from .models import Internship, Project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title' ,'featured_image', 'description' , 'demo_link' , 'source_link','tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self , *args , **kwargs):
        super(ProjectForm , self).__init__()

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        self.fields['title'].widget.attrs.update({'class' : 'input'})
class internshipForm(ModelForm):
    class Meta:
        model = Internship
        fields = ['title' ,'featured_image', 'description' , 'source_link','tags']