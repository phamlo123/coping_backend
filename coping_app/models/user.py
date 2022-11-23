from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    MIDDLER = 'MD'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (MIDDLER, 'Middler'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    
    BUSINESS = "DM"
    COMPUTER_SCIENCE = "KR"
    HEALTH = "BV"
    SOCIAL_SCIENCE = "CSSH"
    ENGINEER = "ENG"
    SCIENCE = "SC"
    ARTS = "AMD"
    OTHER = "OTHER"

    #TODO: make names more accurate (maybe a call to neu website?)
    COLLEGE_CHOICES = [
        (BUSINESS, "BUSINESS"), 
        (COMPUTER_SCIENCE, "COMPUTER_SCIENCE"), 
        (HEALTH, "HEALTH"),
        (SOCIAL_SCIENCE, "SOCIAL_SCIENCE"), 
        (ENGINEER, "ENGINEER"), 
        (SCIENCE, "SCIENCE"), 
        (ARTS, "AMD"),
        (OTHER, "OTHER")]

    username = models.CharField(max_length=200, unique=True)
    year = models.CharField(max_length=200, default=FRESHMAN)
    college = models.CharField(max_length=200, default=OTHER)
    #TODO: validate this field by writing a validator
    number_coops_completed=models.IntegerField()
    linkedin = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"id: {self.id} username: {self.username} college: {self.college}"

        
