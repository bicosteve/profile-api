from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    '''manager for user profiles'''

    def create_user(self,email,name,password=None):
        '''create a new user profile'''
        if not email:
            raise ValueError('User must have an email address')

        #normalizing email address
        email=self.normalize_email(email)
        user.self.model(email=email,name=name)

        user.set_password(password) #for password encryption
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''to create and save a new super user with given details for the system'''
        user = self.create_user(email, name, password)

        useer.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''db models for user in the system'''
    email = models.EmailField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):
        '''get users full name'''
        return self.name

    def get_shortname(self):
        '''get users short name'''
        return self.name

    def __str__(self):
        '''return string rep of the user'''
        return self.email