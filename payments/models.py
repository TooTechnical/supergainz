from django.db import models
from users.models import UserProfile


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    interval = models.CharField(max_length=20, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')])

    def __str__(self):
        return f"{self.name} ({self.interval})"
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
