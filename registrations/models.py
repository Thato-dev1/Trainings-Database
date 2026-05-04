from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = None
    company_ID = models.CharField(max_length= 8, unique= True)
    # USERNAME_FIELD = 'company_CDSID'

    def __str__(self):
        return self.first_name +' '+ self.last_name


