# Generated by Django 4.2.3 on 2023-10-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_cart'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]