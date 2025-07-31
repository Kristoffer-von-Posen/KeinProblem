from django.shortcuts import render
from .models import Btwo

# Create your views here.


def index(request):
  return render(request, "menu/index.html", {"Btwo": Btwo.objects.all()})

  





def dQuiz(request):
  return render(request, "menu/dQuiz.html", {"Btwo": Btwo.objects.all()})
