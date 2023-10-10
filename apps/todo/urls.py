from django.urls import path
from django.views.generic import TemplateView
from .views import CustomLoginView

urlpatterns = [
    path('', TemplateView.as_view(template_name='apps.todo/home.html'), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', TemplateView.as_view(template_name='apps.todo/signup.html'), name='signup'),
]
