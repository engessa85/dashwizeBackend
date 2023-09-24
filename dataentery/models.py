from django.db import models
from django.conf import settings
from time import timezone
# Create your models here.

class MtoM(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ebitactual1 = models.IntegerField(default=100)
    ebitactual2 = models.IntegerField(default=100)
    ebitactual3 = models.IntegerField(default=100)
    ebitactual4 = models.IntegerField(default=100)
    ebitactual5 = models.IntegerField(default=100)
    ebitactual6 = models.IntegerField(default=100)
    ebitactual7 = models.IntegerField(default=100)
    ebitactual8 = models.IntegerField(default=100)
    ebitactual9 = models.IntegerField(default=100)
    ebitactual10 = models.IntegerField(default=100)
    ebitactual11 = models.IntegerField(default=100)
    ebitactual12 = models.IntegerField(default=100)

    ebittarget1 = models.IntegerField(default=100)
    ebittarget2 = models.IntegerField(default=100)
    ebittarget3 = models.IntegerField(default=100)
    ebittarget4 = models.IntegerField(default=100)
    ebittarget5 = models.IntegerField(default=100)
    ebittarget6 = models.IntegerField(default=100)
    ebittarget7 = models.IntegerField(default=100)
    ebittarget8 = models.IntegerField(default=100)
    ebittarget9 = models.IntegerField(default=100)
    ebittarget10 = models.IntegerField(default=100)
    ebittarget11 = models.IntegerField(default=100)
    ebittarget12 = models.IntegerField(default=100)
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email) + " " + str(self.created_at)
    class Meta:
        verbose_name = "MtoM"

class ProfitLoss(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    revenue = models.IntegerField(default=100)
    cost_of_good_sold = models.IntegerField(default=100)
    sales = models.IntegerField(default=100)
    marketing = models.IntegerField(default=100)
    general_and_admin = models.IntegerField(default=100)
    other_income = models.IntegerField(default=100)
    other_expenses = models.IntegerField(default=100)
    interest_and_tax = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email) + " " + str(self.created_at)
    
    def GROSS_PROFIT(self):
        result = self.revenue - self.cost_of_good_sold
        return result
    
    def OPEX(self):
        result = self.sales + self.marketing + self.general_and_admin + self.other_income + self.other_expenses
        return result


