from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import UserForm


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    extra_context = {'title': 'Login Here'}
    success_url = 'home.html'


# class LoginView(generic.FormView):
#     template_name = 'login.html'
#     form_class = UserForm
#     extra_context = {'title': 'Login Page'}
#
#     # def get(self, request):
#     #     form = self.form_class(None)
#     #     context = {'form': form, 'title': 'Login Page'}
#     #     return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#
#             user = authenticate(self.request, username=username, password=password)
#
#             if user is not None and user.is_active:
#                 login(request, user)
#                 if request.GET.get('next'):
#                     return redirect(request.GET.get('next'))
#                 else:
#                     return redirect('dashboard')
#             else:
#                 return render(request, 'error.html', context={'error': "User doesn't exist."})
#
#         if not form.is_valid():
#             user = request.user
#
#             if user is not None:
#                 logout(request)
#                 return redirect('login')
