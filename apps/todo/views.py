from pprint import pprint

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import CustomSignupForm


class CustomAuthenticationForm(AuthenticationForm):

    def is_valid(self):
        res = super().is_valid()
        if not res:
            print(self.errors)
            return res
        return res


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    template_name = 'apps.todo/login.html'
    success_url = "home"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data! Try again or sign up!")
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        pprint(request.POST)
        return super().post(request, *args, **kwargs)


class CustomSignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'apps.todo/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))

        return render(request, self.template_name, {'form': form})
