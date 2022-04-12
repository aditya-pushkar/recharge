from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recharge_plans/', include('recharge_plans.urls')),
    path('prepaid/', include('prepaid.urls')),
    path('dashboard/', include('dashboard.urls')),
]
