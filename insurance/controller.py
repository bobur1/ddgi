from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


@login_required
def home(request):
    return render(request, "home.html")


def individual_client(request):
    return render(request, "individual_client/index.html")


def individual_client_add(request):
    return render(request, "individual_client/add.html")
