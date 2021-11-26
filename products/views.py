from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .serializers import CondutorSerializer
from .models import Condutor, Viatura, Chapa
from rest_framework import viewsets
from .forms import CondutorForm, ViaturaForm, ChapaForm


class CondutorView(viewsets.ModelViewSet):
    queryset = Condutor.objects.all()
    serializer_class = CondutorSerializer


def home(request):
    obj = Viatura.objects.all()
    condutor = Condutor.objects.all()
    chapa = Chapa.objects.all()

    context = {
        'obj': obj,
        'condutor': condutor,
        'chapa':chapa,
    }
    return render(request, 'home.html', context)

def create_form(request):
    form = CondutorForm()
    if request.method == "POST":
        form = CondutorForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "partials/form.html", context)

def carro(request):
    form = ViaturaForm()
    if request.method == "POST":
        form = ViaturaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "partials/viatura_form.html", context)

def chapa(request):
    form = ChapaForm()
    if request.method == "POST":
        form = ChapaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "partials/chapa_form.html", context)
