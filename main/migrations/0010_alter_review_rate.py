# Generated by Django 5.1.1 on 2024-11-01 12:56

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_orders_method_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.SmallIntegerField(db_default=django.db.models.expressions.CombinedExpression(models.F('start'), '+', models.Value(50))),
        ),
    ]
