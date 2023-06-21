from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Artic2


@login_required
def index(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/index.html', {'item': item})


def categ2(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ2.html', {'item': item})


def categ3(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ3.html', {'item': item})


def categ4(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ4.html', {'item': item})


def categ5(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ5.html', {'item': item})


def categ6(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ6.html', {'item': item})


def categ7(request):
    item = Artic2.objects.all()
    return render(request, 'maimmagazi/categ7.html', {'item': item})


def Registrat(request):
    return render(request, 'maimmagazi/Registrat.html')





