from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LogEntry
import json
from django.utils.timezone import now


# Функция для записи лога
def create_log_entry(instance, operation, user=None):
    table_name = instance._meta.model_name  # Имя модели (таблицы)
    record_id = instance.pk  # ID измененной записи
    details = {}

    # Добавляем данные модели, преобразованные в словарь (если нужно)
    if operation != 'DELETE':
        details = {field.name: getattr(instance, field.name) for field in instance._meta.fields}

    # Создаем запись в логе
    LogEntry.objects.create(
        table_name=table_name,
        operation=operation,
        record_id=record_id,
        timestamp=now(),
        user=user,
        details=details
    )


# Обработчик сигнала после сохранения
@receiver(post_save)
def log_create_or_update(sender, instance, created, **kwargs):
    user = None  # Здесь можно передать имя пользователя, если оно доступно (например, из сессии)

    if created:
        create_log_entry(instance, operation='INSERT', user=user)
    else:
        create_log_entry(instance, operation='UPDATE', user=user)


# Обработчик сигнала после удаления
@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    user = None  # Здесь можно передать имя пользователя, если оно доступно (например, из сессии)
    create_log_entry(instance, operation='DELETE', user=user)