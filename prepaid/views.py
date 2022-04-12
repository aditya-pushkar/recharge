from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Recharge
from recharge_plans.models import Plans
from .serializers import RechargeSerializer



# recharge the number 
@api_view(['POST'])
def activate(request):
    try:
        print('hello')
        data = request.data
        phone_num = data.get('phone_num'),
        plan_id = data.get('plan_id'),
        paid = data.get('paid')

        # we get tuples as data but before saving data we have to convert them into sigle string
        phone_num = phone_num[0]
        plan_id = plan_id[0]

        plan_check = Plans.objects.get(id=str(plan_id))
        if plan_check:

            rech  = Recharge.objects.create(
                number = phone_num,
                plan = plan_check,
                paid = paid
            )
            serializer = RechargeSerializer(rech, many=False)
            print('Your plan have been activated')
            print(f'Plan Details: {rech.plan.description}')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

