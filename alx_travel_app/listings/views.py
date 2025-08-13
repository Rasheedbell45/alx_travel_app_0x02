import requests
from rest_framework.views import APIView
from .models import Payment

class InitiatePaymentView(APIView):
    def post(self, request):
        # Make POST request to Chapa API with booking details
        # Store transaction ID and set status to "Pending"
        pass

class VerifyPaymentView(APIView):
    def post(self, request, transaction_id):
        # Verify payment status with Chapa API
        # Update payment status in Payment model
        pass
