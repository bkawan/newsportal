from django import forms

from content.models import PostItem


class PostForm(forms.ModelForm):
    class Meta:
        model = PostItem
        fields = ['title', 'content']
