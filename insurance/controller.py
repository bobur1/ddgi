from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def individual_client(request):
    return render(request, "individual_client/index.html")


def individual_client_add(request):
    return render(request, "individual_client/add.html")
