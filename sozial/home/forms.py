from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Profile, Comment
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label= 'Username',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text',
            'placeholder' : 'username'
        })
    )
    email = forms.EmailField(
        label= 'Email',
        widget= forms.EmailInput(attrs={
            'class' : 'form-control',
            'type' : 'email',
            'placeholder' : 'email'
        })
    )
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type' : 'password',
            'placeholder' : 'password'
        })
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type' : 'password',
            'placeholder' : 'password'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileModelForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text',
            'placeholder' : 'full name'
        })
    )
    image = forms.FileField(
        label= 'Upload image',
        widget= forms.FileInput(attrs={
            'class' : 'form-control',
            'type' : 'file',
            'accept' : 'image/jpeg, image/png'
        })
    )
    bio = forms.CharField(
        label= 'About You',
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'rows' : 4,
            'placeholder': 'about yourself'
        })
    )
    location = forms.CharField(
        label='Address',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text',
            'placeholder' : 'address'
        })
    )
    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'location']
        exclude = ['user', 'id_user']

class CommentModelForm(forms.ModelForm):
    comment_body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class' : 'form-control',
            'rows' : 2
        })
    )
    class Meta:
        model = Comment
        fields = ['comment_body']
        exclude = ['comment_on', 'comment_by', 'comment_date']