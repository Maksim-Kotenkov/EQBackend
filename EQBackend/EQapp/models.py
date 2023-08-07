from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import UserManager


class EQUser(AbstractBaseUser):
    username = models.TextField(
        verbose_name='Никнейм',
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )

    email = models.EmailField(
        max_length=254,
        unique=True
    )

    first_name = models.TextField(
        verbose_name='Имя',
        null=False,
        blank=False,
        max_length=100
    )

    last_name = models.TextField(
        verbose_name='Фамилия',
        null=False,
        blank=False,
        max_length=100
    )

    parent_name = models.TextField(
        verbose_name='Отчество',
        null=False,
        blank=False,
        max_length=100
    )

    gender = models.TextField(
        verbose_name='Пол',
        null=False,
        blank=False,
        max_length=6,
        choices=(
            ('male', 'Мужской'),
            ('female', 'Женский'),
        )
    )

    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        null=False,
        blank=False,
    )

    phone_number = PhoneNumberField(
        verbose_name='Телефон',
        null=False,
        blank=False
    )

    current_test = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Номер текущего теста"
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'parent_name',
        'gender',
        'date_of_birth',
        'phone_number',
    ]

    objects = EQUserManager()

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.parent_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
