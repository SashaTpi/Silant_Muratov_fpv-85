from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    CLIENT = 'Клиент'
    SERVICE = 'Сервис'
    MANAGER = 'Менеджер'
    ADMIN = 'Админ'

    CHOICES = [
        (CLIENT, 'Клиент'),
        (SERVICE, 'Сервисная организация'),
        (MANAGER, 'Менеджер'),
        (ADMIN, 'Админ'),
    ]

    role = models.CharField('Роль пользователя', max_length=10, choices=CHOICES, default='Клиент')
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='users_custom_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='users_custom_users')


    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.username
