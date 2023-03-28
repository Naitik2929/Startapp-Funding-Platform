from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Campaign,Investment
from .forms import CampaignForm, InvestmentForm
from datetime import date
from decimal import Decimal
from django.db.models import Q

@login_required
def campaign_list(request):
    query = request.GET.get('q')
    if query:
        campaigns = Campaign.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        campaigns = Campaign.objects.filter(closed=False).order_by('-created_at')
    closed_campaigns = Campaign.objects.filter(closed=True).order_by('-created_at')
    context = {
        'campaigns': campaigns,
        'closed_campaigns':closed_campaigns
    }
    return render(request, 'campaign_list.html', context)

@login_required
def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    # investor_count = campaign.investors.all().distinct().count()
    # investor_count = campaign.investors.all().count()
    left=(campaign.end_date-date.today()).days
    if left<=0:
            campaign.closed=True
            campaign.save()
    cur=(campaign.current_amount/campaign.goal_amount)*100
    campaign.video_link=convert_to_embed(campaign.video_link)
    context = {
    'campaign': campaign,
    # 'subscribers':investor_count,
    'left_days':left,
    'cur':cur
     }
    return render(request, 'campaign_detail.html', context)


@login_required
def invest(request,id):
    campaign = get_object_or_404(Campaign, id=id)
    if request.method == 'POST':
        amount=Decimal(request.POST.get('amount'))
        investment=Investment.objects.create(
            investor=request.user,
            campaign=campaign,
            amount=amount
        )
        campaign.current_amount += amount
        campaign.subscribers+=1
        campaign.save()
        messages.success(request, 'Thank you for your investment!')
        return redirect('dashboard')
    else:
        context = {'campaign': campaign}
        return render(request, 'invest.html', context)

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

def convert_to_embed(link):
    if 'watch?v=' in link:
        link = link.split('watch?v=')[1]
    elif 'youtu.be/' in link:
        link = link.split('youtu.be/')[1]
    embed_link = f'https://www.youtube.com/embed/{link}'
    return embed_link