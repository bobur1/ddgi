from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from insurance.models import Currency, Policy, InsuranceOffice, PolicySeriesType, User, OfficeWorkers, PolicyTransfers, \
    Vid, IndividualClient, LegalClient, Position, ProductTypeCode, OfficeType, Bank, ProductType, ProductField

@login_required
def home(request):
    return render(request, "home.html")


@login_required
def individual_client(request):
    return render(request, "individual_client/index.html")


@login_required
def individual_client_add(request):
    currency_list = Currency.objects.all()
    return render(request, "individual_client/add.html", {'curr_list': currency_list})


@login_required
def individual_client_show(request, id):
    client = IndividualClient.objects.filter(id=id).first()
    return render(request, "individual_client/show.html", { 'client': client })


@login_required
def individual_client_edit(request, id):
    client = IndividualClient.objects.filter(id=id).first()
    return render(request, "individual_client/edit.html", {
        'client': client,
    })


@login_required
def legal_client(request):
    return render(request, "legal_client/index.html")


@login_required
def legal_client_add(request):
    positions = Position.objects.all()
    return render(request, "legal_client/add.html", {
        'positions': positions,
    })


@login_required
def legal_client_show(request, id):
    client = LegalClient.objects.filter(id=id).first()
    return render(request, "legal_client/show.html", { 'client': client })


@login_required
def legal_client_edit(request, id):
    client = LegalClient.objects.filter(id=id).first()
    users = User.objects.get()
    return render(request, "legal_client/edit.html", {
        'client': client,
        'users': users
    })


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
def request(request):
    return render(request, "request/add.html")

@login_required
def user (request):
    return render(request, "user/add.html")


@login_required
def bank(request):
    return render(request, "references/bank/index.html")


@login_required
def bank_add(request):
    return render(request, "references/bank/add.html")


@login_required
def bank_show(request, id):
    bank = Bank.objects.filter(id=id).first()
    return render(request, "references/bank/show.html", { 'bank': bank })


@login_required
def bank_edit(request, id):
    bank = Bank.objects.filter(id=id).first()
    return render(request, "references/bank/edit.html", { 'bank': bank })


@login_required
def currency(request):
    return render(request, "references/currency/index.html")


@login_required
def currency_add(request):
    return render(request, "references/currency/add.html")


@login_required
def currency_show(request, id):
    currency = Currency.objects.filter(id=id).first()
    return render(request, "references/currency/show.html", { 'currency': currency })


@login_required
def currency_edit(request, id):
    currency = Currency.objects.filter(id=id).first()
    return render(request, "references/currency/edit.html", { 'currency': currency })


@login_required
def view(request):
    return render(request, "references/view/index.html")


@login_required
def view_add(request):
    return render(request, "references/view/add.html")


@login_required
def view_show(request, id):
    view = Vid.objects.filter(id=id).first()
    return render(request, "references/view/show.html", { 'view': view })


@login_required
def view_edit(request, id):
    view = Vid.objects.filter(id=id).first()
    return render(request, "references/view/edit.html", { 'view': view })


@login_required
def klass(request):
    return render(request, "references/klass/index.html")


@login_required
def klass_add(request):
    return render(request, "references/klass/add.html")


@login_required
def klass_show(request, id):
    klass = ProductTypeCode.objects.filter(id=id).first()
    return render(request, "references/klass/show.html", { 'klass': klass })


@login_required
def klass_edit(request, id):
    klass = ProductTypeCode.objects.filter(id=id).first()
    return render(request, "references/polis-series/edit.html", { 'klass': klass })


@login_required
def polis_series(request):
    return render(request, "references/polis-series/index.html")


@login_required
def polis_series_add(request):
    return render(request, "references/polis-series/add.html")


@login_required
def polis_series_show(request, id):
    polisSeries = PolicySeriesType.objects.filter(id=id).first()
    return render(request, "references/polis-series/show.html", { 'polisSeries': polisSeries })


@login_required
def polis_series_edit(request, id):
    polisSeries = PolicySeriesType.objects.filter(id=id).first()
    return render(request, "references/klass/edit.html", { 'polisSeries': polisSeries })
#
#
# @login_required
# def group(request):
#     return render(request, "references/view/index.html")
#
#
# @login_required
# def group_add(request):
#     return render(request, "references/group/add.html")
#
#
# @login_required
# def group_show(request, id):
#     group = Group.objects.filter(id=id).first()
#     return render(request, "references/group/show.html", { 'group': group })
#
#
# @login_required
# def group_edit(request, id):
#     group = Group.objects.filter(id=id).first()
#     return render(request, "references/group/edit.html", { 'group': group })


@login_required
def position(request):
    return render(request, "references/view/index.html")


@login_required
def position_add(request):
    return render(request, "references/position/add.html")


@login_required
def position_show(request, id):
    position = Position.objects.filter(id=id).first()
    return render(request, "references/position/show.html", { 'position': position })


@login_required
def position_edit(request, id):
    position = Position.objects.filter(id=id).first()
    return render(request, "references/position/edit.html", { 'position': position })


@login_required
def branch(request):
    return render(request, "references/branch/index.html")


@login_required
def branch_add(request):
    users = User.objects.all()
    officeTypes = OfficeType.objects.all()
    parentBranches = InsuranceOffice.objects.all()
    # regions = Region.objects.all()
    return render(request, "references/branch/add.html", {
        'users': users,
        'officeTypes': officeTypes,
        'parentBranches': parentBranches,
    })


@login_required
def branch_show(request, id):
    branch = InsuranceOffice.objects.filter(id=id).first()
    return render(request, "references/branch/show.html", { 'branch': branch })


@login_required
def branch_edit(request, id):
    branch = InsuranceOffice.objects.filter(id=id).first()
    users = User.objects.get()
    officeTypes = OfficeType.objects.all()
    parentBranches = InsuranceOffice.objects.exclude(id=id)
    return render(request, "references/branch/edit.html", {
        'branch': branch,
        'users': users,
        'officeTypes': officeTypes,
        'parentBranches': parentBranches,
    })


@login_required
def product(request):
    return render(request, "product/index.html")


@login_required
def product_add(request):
    return render(request, "product/add.html")


@login_required
def product_show(request, id):
    product = ProductType.objects.filter(id=id).first()
    return render(request, "product/show.html", { 'product': product })


@login_required
def product_edit(request, id):
    product = ProductType.objects.filter(id=id).first()
    return render(request, "product/edit.html", { 'product': product })
