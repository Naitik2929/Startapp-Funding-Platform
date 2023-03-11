from django.db import models
from django.contrib.auth.models import User
import datetime

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.IntegerField()
    current_amount = models.IntegerField(default=0)
    start_date = models.DateField(default=datetime.datetime.now)
    end_date = models.DateField()
    # image = models.OneToOneField('Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='campaign')
    image = models.ImageField(upload_to='media', blank=True, null=True)
    video_link = models.URLField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    investors = models.ManyToManyField(User, blank=True, related_name='invested_campaigns')

    def __str__(self):
        return self.name

class Investment(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='investments_made')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE,related_name='investments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} invested {self.amount} in {self.campaign}"

# class Image(models.Model):
#     image = models.ImageField(upload_to='media')

#     def __str__(self):
#         return self.image.name