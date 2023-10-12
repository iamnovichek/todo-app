from django.contrib.auth.forms import UserCreationForm as SignupForm
from django import forms

from .models import CustomUser, Task


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


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=False)
    completed = forms.CheckboxInput()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'completed',
            'completed'
        ]

    def save(self, commit=True):
        if commit:
            new_task = Task.objects.create(
                user=self.user,
                title=self.cleaned_data['title'],
                description=self.cleaned_data['description'],
                completed=self.cleaned_data['completed']
            )
