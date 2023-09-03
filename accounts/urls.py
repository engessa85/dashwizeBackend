from django.urls import path
from .views import SignupView, UserPaymentInfoView

urlpatterns = [
    path("signup", SignupView.as_view()),
    path("paymentinfo",UserPaymentInfoView.as_view())
]
