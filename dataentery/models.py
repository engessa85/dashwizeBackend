from django.db import models
from django.conf import settings
from time import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class MtoM(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ebitactual1 = models.IntegerField(default=1000)
    ebitactual2 = models.IntegerField(default=5000)
    ebitactual3 = models.IntegerField(default=2000)
    ebitactual4 = models.IntegerField(default=3000)
    ebitactual5 = models.IntegerField(default=3000)
    ebitactual6 = models.IntegerField(default=4000)
    ebitactual7 = models.IntegerField(default=3000)
    ebitactual8 = models.IntegerField(default=4000)
    ebitactual9 = models.IntegerField(default=4000)
    ebitactual10 = models.IntegerField(default=3000)
    ebitactual11 = models.IntegerField(default=4000)
    ebitactual12 = models.IntegerField(default=3500)

    ebittarget1 = models.IntegerField(default=1000)
    ebittarget2 = models.IntegerField(default=1500)
    ebittarget3 = models.IntegerField(default=2000)
    ebittarget4 = models.IntegerField(default=2500)
    ebittarget5 = models.IntegerField(default=3000)
    ebittarget6 = models.IntegerField(default=3500)
    ebittarget7 = models.IntegerField(default=4000)
    ebittarget8 = models.IntegerField(default=4500)
    ebittarget9 = models.IntegerField(default=5000)
    ebittarget10 = models.IntegerField(default=5500)
    ebittarget11 = models.IntegerField(default=6000)
    ebittarget12 = models.IntegerField(default=6500)
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    demo = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.email) + " " + str(self.created_at)
    class Meta:
        verbose_name = "MtoM"

class ProfitLoss(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    revenue = models.IntegerField(default=567304)
    cost_of_good_sold = models.IntegerField(default=119129)
    sales = models.IntegerField(default=193760)
    marketing = models.IntegerField(default=66382)
    general_and_admin = models.IntegerField(default=66358)
    other_income = models.IntegerField(default=-1448)
    other_expenses = models.IntegerField(default=6823)
    interest_and_tax = models.IntegerField(default=25015)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    demo = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.email) + " " + str(self.created_at)
    
    def GROSS_PROFIT(self):
        result = self.revenue - self.cost_of_good_sold
        return result
    
    def OPEX(self):
        result = self.sales + self.marketing + self.general_and_admin + self.other_income + self.other_expenses
        return result


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_mtom(sender, instance, created, **kwargs):
    if created:
        MtoM.objects.create(user = instance, demo = True)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_profitLoss(sender, instance, created, **kwargs):
    if created:
        ProfitLoss.objects.create(user = instance, demo = True)