from django.db import models


# Create your models here.
class FraudCheckLog(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    amount = models.FloatField()
    risk_score = models.CharField(max_length=10)  # "low", "medium", "high"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}:{self.risk_score}"
