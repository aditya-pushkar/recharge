from django.urls import path

app_name = 'activate_plan'

from .views import activate

urlpatterns = [
    path('activate/', activate, name='activate_plan')
]
