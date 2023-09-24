from django.urls import path
from .views import MtoMView, ProfitLossView

urlpatterns = [
    path("mtm", MtoMView.as_view()),
    path("profitloss", ProfitLossView.as_view()),
]
