# Generated by Django 5.0.2 on 2024-03-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_is_approved_company_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
