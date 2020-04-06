from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _


class Basemanager(BaseUserManager):
    def create_user(self,email,password,**kwargs):
        if not self.email:
            raise ValueError("You can't blank this email")

        else:
            #self.username=None
            self.password=password
            user=User(email=self.normalize_email(email),**kwargs)#,username=self.username)
            user.set_password(self.password)
            user.save()
        return user

    def create_superuser(self,email,password,**kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)


        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email=email,password=password,**kwargs)


class User(AbstractUser):
    username = models.CharField(max_length=30,blank=True,null=True)
    email    = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = Basemanager

    def __str__(self):
        return self.email

    class Meta:
        db_table='User'
