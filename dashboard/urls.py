from django.urls import path
from .views import (
    recharge_plan_create,
    recharge_plan_delete,
    recharge_plan_update
)

app_name = 'dashboard'

urlpatterns = [
    path('plan/create/', recharge_plan_create, name='plan_create'),
    path('plan/delete/<str:plan_id>/', recharge_plan_delete, name='plan_delete'),
    path('plan/update/<str:plan_id>/', recharge_plan_update, name='plan_update'),
]


