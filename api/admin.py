from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Currency, GoalType, Goal, TransactionCategory, OperationType, PayingMethod, Transaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'full_name', 'email')  # Отображаемые поля
    search_fields = ('login', 'full_name', 'email')  # Поиск по полям
    list_filter = ('full_name', 'email')  # Фильтр по полям


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Поля для отображения в списке


@admin.register(GoalType)
class GoalTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')  # Поля для отображения


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'amount', 'currency', 'goal_type')
    search_fields = ('name',)
    list_filter = ('currency', 'goal_type')


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(PayingMethod)
class PayingMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'method')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'category', 'amount', 'currency', 'datetime')
    search_fields = ('name', 'user__full_name')
    list_filter = ('category', 'currency', 'datetime')
    date_hierarchy = 'datetime'  # Позволяет фильтровать по дате
