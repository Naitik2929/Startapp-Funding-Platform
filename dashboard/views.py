from django.views.generic import TemplateView
from campaign.models import Campaign, Investment
from datetime import date,timedelta
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_investments = Investment.objects.filter(investor=user)
        end_date = date.today() + timedelta(days=7)
        campaigns_closing_soon = Campaign.objects.filter(closed=False, end_date__range=[date.today(), end_date])
        invested_campaigns = [inv.campaign for inv in user_investments]
        invested_campaigns=list(set(invested_campaigns))
        context['invested_campaigns'] = invested_campaigns
        context['campaigns_closing_soon'] = campaigns_closing_soon
        return context

    # def dashboard(request):
    # campaigns_closing_soon = Campaign.objects.filter(
    #     closed=False,
    #     end_date__lte=date.today() + timedelta(days=7)
    # ).order_by('end_date')
    # context = {'campaigns_closing_soon': campaigns_closing_soon}
    # return render(request, 'dashboard.html', context)