from django import forms
from .models import Campaign,Investment
# from .models import Campaign,Image

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('name', 'description', 'goal_amount', 'end_date', 'image', 'video_link','pitch_pdf')
        widgets = {'end_date': forms.DateInput(attrs={'type': 'date'}),
                   'description':forms.Textarea(attrs={'rows':'4'}),
                   'name':forms.TextInput(attrs={'placeholder': "Enter company's registered name here"}),
                   'goal_amount':forms.TextInput(attrs={'placeholder': "Enter Goal Amount"}),
                   'video_link':forms.TextInput(attrs={'placeholder': 'https://www.youtube.com/embed/tgbNymZ7vqY'}),
                   }
        labels = {
            'name': 'Campaign Name',
            'description': 'Describer Your Project',
            'goal_amount': "Campaign's Goal Amount",
            'end_date': "Campaign's Ending Date",
            'image': "Campaign's Logo",
            'video_link': "Campaign's Video Link",
            'pitch_pdf': "Upload your Pitch",
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