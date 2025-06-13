from django.contrib import admin

from .models import FraudCheckLog


# Register your models here.
@admin.register(FraudCheckLog)
class FraudCheckLogAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "ip_address",
        "amount",
        "risk_score",
        "created_at",
    )
    search_fields = ("full_name", "email", "ip_address", "risk_score")
    list_filter = ("risk_score", "created_at")
