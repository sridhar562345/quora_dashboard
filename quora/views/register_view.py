from django.shortcuts import render, redirect
from django.contrib.auth import login
from quora.forms.user_registration import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("question_list")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
