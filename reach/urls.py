"""
URL configuration for reach project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    UserViewSet, CurrencyViewSet, GoalTypeViewSet, GoalViewSet,
    TransactionCategoryViewSet, OperationTypeViewSet, PayingMethodViewSet, TransactionViewSet
)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'goal-types', GoalTypeViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'transaction-categories', TransactionCategoryViewSet)
router.register(r'operation-types', OperationTypeViewSet)
router.register(r'paying-methods', PayingMethodViewSet)
router.register(r'transactions', TransactionViewSet)
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/sql/', views.export_sql, name='export_sql'),
    path('import/csv/', views.import_csv, name='import_csv'),
    path('import/sql/', views.import_sql, name='import_sql'),
]
