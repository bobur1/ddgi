from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from insurance.models import Currency, RegisteredPolises, Branch

def home(request):
    return render(request, "home.html")


def individual_client(request):
    return render(request, "individual_client/index.html")


def individual_client_add(request):
    currency_list = Currency.objects.all()
    return render(request, "individual_client/add.html", {'curr_list': currency_list,
                                                          'name': 'Shohrux'})


def legal_client(request):
    return render(request, "legal_client/index.html")


def legal_client_add(request):
    return render(request, "legal_client/add.html")


def polis_registration(request):
    return render(request, "polis_registration/index.html")


def polis_registration_add(request):
    return render(request, "polis_registration/add.html", {
        'policy': None,
    })


def polis_transfer_list(request):
    return render(request, "polis_transfer/index.html")


def polis_transfer(request):
    polises = RegisteredPolises.objects.all()
    offices = Branch.objects.all()
    return render(request, "polis_transfer/transfer.html", {
        'polises': polises,
        'offices': offices,
    })
