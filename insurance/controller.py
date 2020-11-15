from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from insurance.models import Currency, Policy, InsuranceOffice, PolicySeriesType, User

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
    polis_series = PolicySeriesType.objects.all()
    return render(request, "polis_registration/add.html", {
        'policy': None,
        'polis_series': polis_series,
    })


def polis_transfer_list(request):
    return render(request, "polis_transfer/index.html")


def polis_transfer(request):
    polises = Policy.objects.filter(policytransfers__to_office__isnull=True)
    offices = InsuranceOffice.objects.all()
    return render(request, "polis_transfer/transfer.html", {
        'polises': polises,
        'offices': offices,
    })


def polis_retransfer_list(request):
    return render(request, "polis_retransfer/index.html")


def polis_retransfer(request):
    polises = Policy.objects.filter(policytransfers__to_office__isnull=False)
    users = User.objects.all()
    return render(request, "polis_retransfer/retransfer.html", {
        'polises': polises,
        'users': users,
    })
