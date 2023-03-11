from django import forms
from .models import Campaign,Investment
# from .models import Campaign,Image

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('name', 'description', 'goal_amount', 'end_date', 'image', 'video_link', 'featured')
        widgets = {'end_date': forms.DateInput(attrs={'type': 'date'}),
                   'description':forms.Textarea(attrs={'rows':'5'})
                   }
        labels = {
            'name': 'Campaign Name',
            'description': 'Description',
            'goal_amount': 'Goal Amount',
            'end_date': 'End Date',
            'image': 'Image',
            'video_link': 'Video Link',
            'featured': 'Featured',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, user):
        campaign = super().save(commit=False)
        campaign.created_by = user
        campaign.save()
        return campaign

class InvestmentForm(forms.ModelForm):
    class Meta:
        model=Investment
        fields=['campaign','amount']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def invest(self):
        amount=self.cleaned_data['amount']