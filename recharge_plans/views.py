from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q

from .models import Plans
from .serializers import RechargePlanSerializer

# Create your views here.

@api_view(['GET'])
def get_plans(request):
    try:
        plans = Plans.objects.filter(active=True)
        serializer = RechargePlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_403_FORBIDDEN)


# http://127.0.0.1:8000/recharge_plans/search/?q=2GB
@api_view(['GET'])
def search_plans(request):
    try:
        query = request.query_params.get('q')
        if query == None:
            query == None
        plans = Plans.objects.filter(Q(description__icontains=query))
        serializer = RechargePlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(f"{e}", status=status.HTTP_404_NOT_FOUND)
    


