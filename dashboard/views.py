# THIS DASHBOARD IS ONLY FOR STAF MEMBER 

from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from recharge_plans.models import Plans
from recharge_plans.serializers import RechargePlanSerializer


# Create your views here.

@api_view(['POST'])
def recharge_plan_create(request):
    try:
        if request.user.is_staff == True:
            data = request.data

            description = data.get('description')
            validity = data.get('validity')
            amount = data.get('amount')
            active = data.get('active')

            plan = Plans.objects.create(
                description=description,
                validity=validity,
                amount=amount,
                active=active
            )
            serializer = RechargePlanSerializer(plan, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    except Exception as error:
        return Response(f"{error}", status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def recharge_plan_delete(request, plan_id):
    try:
        if request.user.is_staff == True:
            plan = Plans.objects.get(id=plan_id)
            if plan:
                plan.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"mesage": "plan deleted"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as error:
        return Response(f'{error}', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def recharge_plan_update(request, plan_id):
    try:
        if request.user.is_staff == True:
            plan = Plans.objects.get(id=plan_id)
            serializer = RechargePlanSerializer(plan, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as error:
        return Response(f'{error}', status=status.HTTP_400_BAD_REQUEST)