from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website import forms
from website.models import Record


# Create your views here.
def homeView(request):
    records = Record.objects.all().order_by("-created_at")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "🎈 You are logged in!!")
            return redirect("home")
        else:
            messages.success(
                request, "🚓 Could not log you in, please try again later!"
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def userLogout(request):
    logout(request)
    messages.success(request, "🪬 you have been logged out!")
    return redirect("home")


def userRegister(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "🎀 you are now a Registered user!")
            return redirect("home")
    else:
        form = forms.RegisterForm()
        return render(request, "register.html", {"form": form})


def indiRecord(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "indiRecord.html", {"record": record})
    else:
        return redirect("home")


def deleteRecord(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "🚮 hope that wasn't worth anything")
        return redirect("home")
    else:
        return redirect("home")


def addRecord(request):
    form = forms.AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                addRecord = form.save()
                messages.success(request, "your record was added! 🎀")
                return redirect("home")
        return render(request, "addRecord.html", {"addRecordForm": form})
    else:
        return redirect("home")


def updateRecord(request,pk):
    if request.user.is_authenticated:
        currRecord = Record.objects.get(id=pk)
        form = forms.AddRecordForm(request.POST or None, instance = currRecord)
        if form.is_valid():
            form.save()
            messages.success(request, "your record was updated! 🎀")
            return redirect("home")
        return render(request, "editRecord.html", {"editRecordForm": form})
    else:
        return redirect("home")