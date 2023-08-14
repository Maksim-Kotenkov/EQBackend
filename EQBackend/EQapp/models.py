from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм',
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )

    password = models.CharField(
        max_length=30
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'parent_name',
        'gender',
        'date_of_birth',
        'phone_number',
    ]

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.parent_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tests(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Название теста"
    )

    type = models.CharField(
        max_length=20,
        default="other",
        choices=(
            ("initial", "Начальный/конечный"),
            ("other", "Другой"),
        ),
        blank=False,
        null=False,
        verbose_name="Тип теста"
    )

    number = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Порядковый номер теста"
    )

    test_data = models.TextField(
        default="sum: 30\n"
                "questions:\n"
                "  q1:\n"
                "    text: 'Как вы относитесь к молоку?'\n"
                "    answers:\n"
                "      answer1:\n"
                "        value: 7\n"
                "        text: Нет\n"
                "      answer2:\n"
                "        value: 1\n"
                "        text: Да\n",
        null=False,
        blank=False,
        verbose_name="Данные теста"
    )

    counting_function = models.TextField(
        null=False,
        blank=False,
        verbose_name="Функция подсчета результата",
        default="(() => answer.reduce((sum, current) => sum + current.answer.value, 0))()"
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answers(models.Model):
    user = models.ForeignKey(
        User,
        related_name='answer',
        on_delete=models.CASCADE
    )

    testId = models.IntegerField()

    answers = models.TextField(
        default="q1:\n"
                "  text: Вы выгорели?\n"
                "    answer:\n"
                "      value: 1\n"
                "      text: Да\n",
        null=False,
        blank=False,
        verbose_name="Данные ответа"
    )

    total = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
