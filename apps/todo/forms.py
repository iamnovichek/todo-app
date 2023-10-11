from django.contrib.auth.forms import UserCreationForm as SignupForm
from django import forms

from .models import CustomUser


class CustomSignupForm(SignupForm):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email',
                  'password1',
                  'password2'
                  ]

    def save(self, commit=True):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        if commit:
            user = CustomUser.objects.create_user(
                email=email,
                password=password
            )

            return user
