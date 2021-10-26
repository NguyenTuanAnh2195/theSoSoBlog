from django.db.models.base import Model
from django.forms import ModelForm
from account.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
