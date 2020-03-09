from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
#doctor
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), db_index=True,unique=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    # Flags
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length= 299)
    speciality= models.CharField(max_length=122)
    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctor')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff
    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

