from django.db import models

# Create your models here.
from django.db import models




class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.login


class Currency(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GoalType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    goal_type = models.ForeignKey(GoalType, on_delete=models.SET_NULL, null=True)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class OperationType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class PayingMethod(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self):
        return self.method


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(TransactionCategory, on_delete=models.SET_NULL, null=True)
    operation_type = models.ForeignKey(OperationType, on_delete=models.SET_NULL, null=True)
    paying_method = models.ForeignKey(PayingMethod, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name


from django.db import models