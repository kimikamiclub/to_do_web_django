# Generated by Django 4.2.1 on 2023-05-25 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('due_date', models.DateField(default=datetime.datetime(2023, 5, 25, 20, 54, 42, 178315))),
                ('status', models.CharField(choices=[('TO_DO', 'TO_DO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('BLOCK', 'BLOCK')], default='TO_DO', max_length=20)),
                ('category', models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('PERSONAL', 'PERSONAL'), ('SHOPPING', 'SHOPPING'), ('WISHLIST', 'WISHLIST'), ('WORK', 'WORK'), ('SPORT', 'SPORT')], default='DEFAULT', max_length=20)),
            ],
        ),
    ]
