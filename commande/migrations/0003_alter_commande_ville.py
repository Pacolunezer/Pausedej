# Generated by Django 4.2.3 on 2024-04-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_commande_code_pays_commande_total_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='ville',
            field=models.CharField(max_length=200),
        ),
    ]
