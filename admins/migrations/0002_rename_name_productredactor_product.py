# Generated by Django 5.1.1 on 2024-10-25 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productredactor',
            old_name='name',
            new_name='product',
        ),
    ]
