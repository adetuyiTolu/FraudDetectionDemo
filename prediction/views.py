from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import FraudCheckkLogSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .models import FraudCheckLog
from . import predictor


class FraudCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        amount = float(data.get("amount", 0))
        full_name = data.get("full_name")
        email = data.get("email")
        ip = data.get("ip_address")

        # use the model to detect fraud
        risk = predictor.predict(email, amount)

        # log the request now
        FraudCheckLog.objects.create(
            full_name=full_name,
            email=email,
            ip_address=ip,
            amount=amount,
            risk_score=risk,
        )
        return Response({"risk": risk}, status=status.HTTP_200_OK)


class FraudCheckLogListView(generics.ListAPIView):
    queryset = FraudCheckLog.objects.all()
    serializer_class = FraudCheckkLogSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["risk_score"]
    search_fields = ["full_name", "email"]
    ordering_fields = ["created_at", "amount"]
