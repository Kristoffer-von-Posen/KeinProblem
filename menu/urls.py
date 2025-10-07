from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
    path("", views.index, name="index"),
    path("dQuiz", views.dQuiz, name="dQuiz"),
    path("api/words", views.Qwords, name="Qwords")
]
