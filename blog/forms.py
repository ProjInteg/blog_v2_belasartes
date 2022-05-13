from django import forms
from .models import Post

class formulario(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'test',)