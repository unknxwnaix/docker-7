from django.conf import settings
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    User, Currency, GoalType, Goal,
    TransactionCategory, OperationType, PayingMethod, Transaction
)
from .serializers import (
    UserSerializer, CurrencySerializer, GoalTypeSerializer, GoalSerializer,
    TransactionCategorySerializer, OperationTypeSerializer, PayingMethodSerializer, TransactionSerializer
)

import csv
import os
import subprocess


# Экспорт данных в CSV
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="database_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Login', 'Full Name', 'Email'])

    for user in User.objects.all():
        writer.writerow([user.id, user.login, user.full_name, user.email])

    return response


# Экспорт базы данных в SQL
def export_sql(request):
    file_path = os.path.join(settings.BASE_DIR, 'database_dump.sql')
    command = [
        'pg_dump',
        '--dbname=postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(
            USER=settings.DATABASES['default']['USER'],
            PASSWORD=settings.DATABASES['default']['PASSWORD'],
            HOST=settings.DATABASES['default']['HOST'],
            PORT=settings.DATABASES['default']['PORT'],
            NAME=settings.DATABASES['default']['NAME']
        ),
        '-f', file_path
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Ошибка при экспорте базы данных: {e}", status=500)

    with open(file_path, 'r') as dump_file:
        response = HttpResponse(dump_file.read(), content_type='application/sql')
        response['Content-Disposition'] = 'attachment; filename=database_dump.sql'

    os.remove(file_path)
    return response


# Импорт данных из CSV
def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Файл должен быть в формате CSV")

        data = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(data)
        next(reader)

        for row in reader:
            User.objects.create(
                id=row[0],
                login=row[1],
                full_name=row[2],
                email=row[3]
            )

        return HttpResponse("Данные успешно импортированы!")

    return render(request, 'import_csv.html')


# Импорт базы данных из SQL
def import_sql(request):
    if request.method == 'POST':
        sql_file = request.FILES['file']
        if not sql_file.name.endswith('.sql'):
            return HttpResponse("Файл должен быть в формате SQL")

        sql_data = sql_file.read().decode('utf-8')
        with connection.cursor() as cursor:
            cursor.execute(sql_data)

        return HttpResponse("SQL успешно импортирован!")

    return render(request, 'import_sql.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class GoalTypeViewSet(viewsets.ModelViewSet):
    queryset = GoalType.objects.all()
    serializer_class = GoalTypeSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class TransactionCategoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategorySerializer


class OperationTypeViewSet(viewsets.ModelViewSet):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer


class PayingMethodViewSet(viewsets.ModelViewSet):
    queryset = PayingMethod.objects.all()
    serializer_class = PayingMethodSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer