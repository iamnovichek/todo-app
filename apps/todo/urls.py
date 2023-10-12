from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (CustomLoginView, CustomSignupView, CreateTaskView,
                    ListTasksView, DeleteTaskView)

urlpatterns = [
    path('', ListTasksView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
]
