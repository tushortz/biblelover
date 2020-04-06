from django.db import models

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MemberManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(
        'Country', on_delete=models.SET_NULL, null=True)
    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return "{} {}".format(self.first_name.strip(), self.last_name.strip())

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
