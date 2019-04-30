from django import forms
from .models import Post, Photo
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

class AdminPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)
            
# class AlbumForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')    
#     class Meta:
#         model = Album
#         fields = ('name', 'description',)


# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')    
#     class Meta:
#         model = Images
#         fields = ('image', )
