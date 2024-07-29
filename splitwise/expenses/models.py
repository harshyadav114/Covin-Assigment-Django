from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    name = models.CharField(max_length=150, blank=False, null=False)
    phone_number = PhoneNumberField(blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email.lower()
        
        return super(User, self).save(*args, **kwargs)
    

    def check_password(self, raw_password: str) -> bool:
        return super().check_password(raw_password)


class IndividualExpense(models.Model):
    user = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class Type(models.TextChoices):
    exact = "EXACT"
    equal = "EQUAL"
    percentage = "PERCENTAGE"


class Expense(models.Model):
    description = models.CharField(max_length=150)
    total_amount = models.PositiveIntegerField()
    type = models.CharField(max_length=150, choices=Type,
                            blank=False, null=False)
    individual_expenses = models.ForeignKey(
        IndividualExpense, blank=False, null=True, on_delete=models.SET_NULL)
    payed_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)
