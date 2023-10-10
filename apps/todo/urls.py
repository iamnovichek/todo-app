from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    path('', TemplateView.as_view(template_name='apps.todo/home.html'), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', TemplateView.as_view(template_name='apps.todo/signup.html'), name='signup'),
]
