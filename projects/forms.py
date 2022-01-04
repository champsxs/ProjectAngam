from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Projects
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'demo_link': forms.TextInput(attrs={'class': 'form-control'}),
            'source_link': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
             

        }
    
    # def __init__(self, *args, **kwargs ):
    #     super(ProjectForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         inputtype = field.widget.__class__.__name__
    #         if "TextInput" in inputtype:
    #             field.widget.attrs.update({'type': 'text'})
    #             field.widget.attrs.update({'class':'form-control col-sm-6'})
    #         if "CheckboxSelectMultiple" in inputtype:
    #             field.widget.attrs.update({'type':'checkbox'})
    #             field.widget.attrs.update({'class':'form-control '})
    #         if "ClearableFileInput" in inputtype:
    #             field.widget.attrs.update({'type': 'file'})
    #             field.widget.attrs.update({'class': 'form-control-file'})
    #         else:
    #             field.widget.attrs.update({'class':'form-control'})
            