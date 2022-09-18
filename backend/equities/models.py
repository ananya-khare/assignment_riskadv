from django.db import models

# Create your models here.
class Equity(models.Model):
    equity_id = models.CharField(max_length=30)
    equity_name = models.CharField(max_length=500)
    equity_desc = models.CharField(max_length=5000)

class returns(models.Model):
    equity = models.ForeignKey(Equity,on_delete=models.CASCADE)
    open = models.FloatField()
    close = models.FloatField()
    day_return = models.FloatField()