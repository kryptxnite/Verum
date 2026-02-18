from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'full-width',
                'placeholder': 'Your Name',
                'name': 'cName'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'full-width',
                'placeholder': 'Your Email',
                'name': 'cEmail'
            }),
            'body': forms.Textarea(attrs={
                'class': 'full-width',
                'placeholder': 'Your Comment',
                'name': 'cMessage'
            }),
        }