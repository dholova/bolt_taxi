from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Створення та збереження нового користувача з email та паролем
        """
        if not email:
            raise ValueError('Email повинен бути вказаний')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.save(using=self._db)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def get_user_model(self):
        return get_user_model()

    def get_by_natural_key(self, email):
        return self.get(email=email)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20)
    car_in_fleet = models.CharField(max_length=255)
    confirmed = models.BooleanField(default=False, )
    language = models.CharField(max_length=255)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=255, default='Kyiv')
    language_2 = models.CharField(max_length=255, default='Ukrainian')

    billing_type = models.CharField(max_length=255, default='Company')
    company_name = models.CharField(max_length=250, default='')
    person_name = models.CharField(max_length=250, default='')
    address = models.CharField(max_length=250, default='')
    registration_code = models.CharField(max_length=50, default='')
    vat_liability = models.CharField(max_length=20, default='')
    vat_number = models.CharField(max_length=50, default='')
    bank_acc_holder_name = models.CharField(max_length=50, default='')
    bank_acc = models.CharField(max_length=50, default='')
    bic_swift = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def has_perm(self, perm, obj=None):
         """
         Повернення True, якщо користувач має дозвіл на виконання дії.
         """
         return True

    def has_module_perms(self, app_label):
         """
         Повернення True, якщо користувач має дозвіл на доступ до "app_label".
         """
         return True


