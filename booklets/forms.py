from django import forms
from .models import Booklet,Category
from django.core.exceptions import ValidationError

class BookletForm (forms.ModelForm):
    class Meta:
        model= Booklet
        fields= "__all__"

    def clean_title(self):
        title=self.cleaned_data.get("title")
        if len(title)>=10 and len(title)<=50:
            return title
        raise ValidationError("Title must be between 10 to 50 characters !!")


    def clean(self):
        super(BookletForm,self).clean()
        content=self.cleaned_data.get('content')
        if len(content) < 2:
            raise ValidationError("Content must be greater than 2 characters !!")
        return self.cleaned_data     


class CategoryForm(forms.ModelForm):
    def clean(self):
        super(CategoryForm,self).clean()
        name=self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError("Category name must be greater than 2 characters !!")
        return self.cleaned_data 


