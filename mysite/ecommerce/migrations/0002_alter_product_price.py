# Generated by Django 3.2 on 2021-04-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
