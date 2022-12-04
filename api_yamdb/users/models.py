from django.contrib.auth.models import AbstractUser
from django.db import models


ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
ROLES = [
    (ADMIN, 'Administrator'),
    (MODERATOR, 'Moderator'),
    (USER, 'User'),
]


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150, null=False,
        unique=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        choices=ROLES,
        default=USER,
        max_length=150,
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser or self.is_staff

    @property
    def is_user(self):
        return self.role == USER

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me',
            )
        ]

    def __str__(self):
        return self.username
