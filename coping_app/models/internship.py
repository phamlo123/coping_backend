from django.db import models
from .company import Company

class Internship(models.Model):
    SUMMER = "SM"
    SPRING = "S"
    FALL = "F"

    CYCLE = [(SUMMER, "Summer"), (SPRING, "SPRING"), (FALL, "F")]

    owner = models.ForeignKey('auth.User', related_name="internships", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    pay = models.DecimalField(decimal_places=2, max_digits=8)
    title = models.CharField(max_length=100)
    #TODO: enforce min-max
    co_op_num = models.IntegerField()
    cycle = models.CharField(max_length=2000)
    tasks = models.CharField(max_length=10000)
    drug_test = models.BooleanField(default=False)

        
    