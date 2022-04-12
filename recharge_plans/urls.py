from django.urls import path

app_name='recharge_plans'

from .views import (
    get_plans,
    search_plans
)

urlpatterns = [
    path('all/', get_plans, name='get_plans'),
    path('search/', search_plans, name='search'),
]
