from django import forms
from django.forms import DateTimeInput

from .models import Post, Comment, User


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ('author', 'created_at')
        widgets = {
            'pub_date': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
