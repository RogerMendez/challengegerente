from rest_framework import serializers

# Model Invoice
from invoices.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = ['created', 'modified']
