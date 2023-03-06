@login_required
def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    investor_count = campaign.investors.count()
    invested = False
    if request.user.is_authenticated:
        if request.user.invested_campaigns.filter(id=campaign.id).exists():
            invested = True
    context = {
    'campaign': campaign,
     'invested': invested,
    'subscribers':investor_count,
     }
    return render(request, 'campaign_detail.html', context)

    # invested or not 