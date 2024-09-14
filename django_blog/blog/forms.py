from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extending the UserCreationForm for Registration
class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user        
    

class UserProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email', 'first_name', 'last_name']