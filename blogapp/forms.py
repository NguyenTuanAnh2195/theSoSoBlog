from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

