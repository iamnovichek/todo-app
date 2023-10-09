from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='apps.todo/home.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='apps.todo/login.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='apps.todo/signup.html'), name='signup'),
]
