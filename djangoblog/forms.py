from .models import BlogApp
from django import forms

class BlogForm(forms.ModelForm):
	class Meta:
		model=BlogApp
		fields='__all__'