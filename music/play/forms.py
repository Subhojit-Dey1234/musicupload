from django import forms
from .models import FileUpload, UserDetails,LikesUser, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
class MusicForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('name','file','images')

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class UserAccountForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ('name','profile_image')

class LikeForm(ModelForm):
    class Meta:
        model = LikesUser
        fields ='__all__'

class Commentform(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)