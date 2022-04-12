from email.policy import default
from tabnanny import verbose
from django.db import models
import uuid 

from recharge_plans.models import Plans

# Create your models here.

# recharge the number with pre_paid plan
class Recharge(models.Model):
    number = models.PositiveBigIntegerField(max_length=10)
    plan = models.ForeignKey(Plans, on_delete=models.SET_NULL, null=True)
    paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.plan} {self.paid}"

