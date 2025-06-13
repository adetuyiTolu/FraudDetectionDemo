from django.urls import path
from .views import FraudCheckLogListView, FraudCheckView

urlpatterns = [
    path("check/", FraudCheckView.as_view(), name="fraud_check"),
    path("fraud-logs/", FraudCheckLogListView.as_view(), name="fraud-logs"),
]
