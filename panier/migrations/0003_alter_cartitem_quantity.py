# Generated by Django 4.2.3 on 2023-09-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0002_remove_cartitem_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
