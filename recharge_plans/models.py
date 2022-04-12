from email.policy import default
from tkinter.tix import Tree
from django.db import models
import uuid


# Create your models here.

# RechargePlans
class Plans(models.Model):
    description = models.TextField()
    validity = models.PositiveIntegerField() # total number of days that plans will be valid for.
    amount = models.PositiveIntegerField(default=0) # amount in Rs
    active = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


    def __str__(self):
        return f"₹ { self.amount }  Validity: { self.validity }  { self.description }"