from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'apps.todo/login.html'
    success_url = "home"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data! Try again or sign up!")
        return self.render_to_response(self.get_context_data(form=form))
