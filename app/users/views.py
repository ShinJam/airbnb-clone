from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        print("this is form >>", form)
        return render(request, "users/login.html", {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        print(form)
