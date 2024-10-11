from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.db import models




class User(AbstractUser):
    ROLES = (
        ('users', 'Users'),
        ('admin', 'Admin'),
    )
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=50, choices=ROLES, default='users')
    first_name = models.CharField(max_length =100 )
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length =100 , null = True , blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    
class UploadAssigment(models.Model):
    userobj= models.ForeignKey(User , models.DO_NOTHING,
                                    limit_choices_to={'user_type': 'users'},
                                    related_name='users',
                                    verbose_name='users')
    task = models.CharField(max_length = 100)
    Tagadmin = models.ForeignKey(User , models.DO_NOTHING,
                                    limit_choices_to={'user_type': 'admin'},
                                    related_name='admin',
                                    verbose_name='admin')
    
    
    
    def __str__(self):
        return f"{self.task} assigned by {self.Tagadmin.first_name}"
    