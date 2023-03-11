from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('<int:id>', views.campaign_detail, name='campaign_detail'),
    path('<int:id>/payment/', views.invest, name='payment'),
    path('create', views.create_campaign, name='create_campaign'),
]