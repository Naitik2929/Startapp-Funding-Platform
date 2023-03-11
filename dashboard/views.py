from django.views.generic import TemplateView
from campaign.models import Campaign, Investment
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_investments = Investment.objects.filter(investor=self.request.user)
        invested_campaigns = [inv.campaign for inv in user_investments]
        context['invested_campaigns'] = invested_campaigns
        return context
