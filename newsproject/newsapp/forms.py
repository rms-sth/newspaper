from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=1000)
    password = forms.CharField(widget=forms.PasswordInput)


class AdminNewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'topic', 'image',
                  'content', 'status')
        widgets = {
            'content': SummernoteWidget(),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Say something...'
            }),

        }
