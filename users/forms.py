from django import forms
from .import models
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Incorrect Password!"))
            
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User Does Not Exist!"))


class SignUpForm(UserCreationForm):
    
    username = forms.EmailField(label="Email")