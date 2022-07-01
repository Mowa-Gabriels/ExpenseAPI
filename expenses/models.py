
from django.db import models
from authentication.models import User



class Expense(models.Model):

    OPTIONS = [
        ('ONLINE_SERVICES', 'ONLINE_SERVICES' ),
        ('TRAVEL', 'TRAVEL'),
        ('FOOD', 'FOOD'),
        ('RENT', 'RENT'),
        ('OTHER', 'OTHER'),
    ]

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models. CharField(choices=OPTIONS, max_length=20)
    amount = models.DecimalField(
        max_digits=20, max_length=225, decimal_places=2
    )
    date = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.owner.username


    