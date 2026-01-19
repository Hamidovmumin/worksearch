from django.db import models

class Payment(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=(('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')),
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

