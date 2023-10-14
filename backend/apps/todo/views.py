from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from .forms import CustomSignupForm, CreateTaskForm
from .models import Task


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'apps.todo/login.html'
    success_url = "home"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data! Try again or sign up!")
        return self.render_to_response(self.get_context_data(form=form))


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


class CreateTaskView(CreateView):
    template_name = "apps.todo/create-task.html"
    form_class = CreateTaskForm
    success_url = "home"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data, try again!")
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        messages.success(self.request, "The task was created successfully!")
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('create-task'))

        return render(request, self.template_name, {'form': form})


class ListTasksView(ListView):
    model = Task
    template_name = "apps.todo/home.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
            return context
        except TypeError:
            return context


class DeleteTaskView(DeleteView):
    context_object_name = 'task'
    template_name = "apps.todo/delete-task.html"
    success_url = 'home'
    model = Task

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            super().post(request, *args, **kwargs)
            return redirect(self.success_url)


class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "apps.todo/task-detail.html"

    def get_queryset(self):
        queryset = super(DetailTaskView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['title',
              'description',
              'completed']
    success_url = 'home'
    template_name = "apps.todo/update-task.html"

    def get_queryset(self):
        queryset = super(UpdateTaskView, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect(self.success_url)
