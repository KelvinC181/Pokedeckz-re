from . import views
from django.urls import path

urlpatterns = [
    path('', views.CardLibrary.as_view(), name="home"),
    path("<str:card_id>/", views.card_detail, name="card_detail")
]