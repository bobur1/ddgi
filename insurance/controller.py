from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from insurance.models import Currency, Policy, InsuranceOffice, PolicySeriesType, User, OfficeWorkers, PolicyTransfers

@login_required
def home(request):
    return render(request, "home.html")


@login_required
def individual_client(request):
    return render(request, "individual_client/index.html")


@login_required
def individual_client_add(request):
    currency_list = Currency.objects.all()
    return render(request, "individual_client/add.html", {'curr_list': currency_list,
                                                          'name': 'Shohrux'})


@login_required
def legal_client(request):
    return render(request, "legal_client/index.html")


@login_required
def legal_client_add(request):
    return render(request, "legal_client/add.html")


@login_required
def polis_registration(request):
    return render(request, "polis_registration/index.html")


@login_required
def polis_registration_add(request):
    polis_series = PolicySeriesType.objects.all()
    return render(request, "polis_registration/add.html", {
        'policy': None,
        'polis_series': polis_series,
    })


@login_required
def polis_transfer_list(request):
    return render(request, "polis_transfer/index.html")


@login_required
def polis_transfer(request):
    polises = Policy.objects.filter(policytransfers__to_office__isnull=True)
    offices = InsuranceOffice.objects.all()
    return render(request, "polis_transfer/transfer.html", {
        'polises': polises,
        'offices': offices,
    })


@login_required
def polis_retransfer_list(request):
    return render(request, "polis_retransfer/index.html")


@login_required
def polis_retransfer(request):
    office = InsuranceOffice.objects.filter(director=request.user).first()
    officeWorkers = OfficeWorkers.objects.filter(office=office)
    polisTransfers = PolicyTransfers.objects.filter(to_office=office)
    return render(request, "polis_retransfer/retransfer.html", {
        'polisTransfers': polisTransfers,
        'officeWorkers': officeWorkers,
    })


@login_required
def request (request):
    return render(request, "request/add.html")


@login_required
def spravochnik_bank (request):
    return render(request, "spravochniki/bank/add.html")

@login_required
def user (request):
    return render(request, "user/add.html")


@login_required
def currency(request):
    return render(request, "spravochniki/currency/index.html")


@login_required
def currency_add(request):
    return render(request, "spravochniki/currency/add.html")
