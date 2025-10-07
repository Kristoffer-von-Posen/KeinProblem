from django.shortcuts import HttpResponse, render
from .models import Btwo
from django.http import JsonResponse

# Create your views here.


def index(request):
  return render(request, "menu/index.html", {"Btwo": Btwo.objects.all()})


def dQuiz(request):
  return render(request, "menu/dQuiz.html", {"Btwo": Btwo.objects.all()})


## Btwo.objects.all() DO UZYCIA W ZUKUNFT

xxx = 1
yyy = 2
zzz = "test"
vvv = 3


def Qwords(request):
  Rwords = {'day': xxx, 'week': yyy, 'word': zzz, 'art': vvv}
  return HttpResponse("Hallo Welt")
