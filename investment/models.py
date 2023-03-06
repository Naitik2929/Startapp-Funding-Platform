from django.db import models
from django.contrib.auth.models import User
from campaign.models import Campaign


class Investment(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} invested {self.amount} in {self.campaign}"
