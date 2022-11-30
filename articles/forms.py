from django import forms
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistration(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cldata = self.cleaned_data
        if cldata['password'] != cldata['password2']:
            raise forms.ValidationError('Passwords do not match.')

        return cldata['password2']


class ArticleRegistrationForm(forms.ModelForm):
    class Meta: 
        model = Article
        fields = ('title', 'description')


class ArticleUpdateForm(forms.ModelForm):
    class Meta: 
        model = Article
        fields = ('title', 'description')