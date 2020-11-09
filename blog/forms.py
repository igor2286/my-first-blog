from django import forms
from .models import Post
from .models import CommentPost
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email is being used by another account')
        return email


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text',)

