from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Campaign
from .forms import CampaignForm
# from .forms import CampaignForm, InvestmentForm

@login_required
def campaign_list(request):
    campaigns = Campaign.objects.all().order_by('-created_at')
    context = {'campaigns': campaigns}
    return render(request, 'campaign_list.html', context)

@login_required
def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    investor_count = campaign.investors.count()
    left=(campaign.end_date-campaign.start_date).days
    context = {
    'campaign': campaign,
    'subscribers':investor_count,
    'left_days':left,
     }
    return render(request, 'campaign_detail.html', context)

# def invest(request):

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(request.user)
            messages.success(request, 'Campaign created successfully.')
            return redirect('campaign_detail', campaign.pk)
        else:
            messages.error(request, 'There was an error creating the campaign.')
    else:
        form = CampaignForm()

    context = {'form': form}
    return render(request, 'create_campaign.html', context)