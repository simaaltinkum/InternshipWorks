# Generated by Django 4.2.3 on 2023-08-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseapp', '0007_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(default=1, max_length=50)),
                ('service2', models.CharField(default=1, max_length=50)),
                ('service3', models.CharField(default=1, max_length=50)),
                ('service4', models.CharField(default=1, max_length=50)),
                ('service5', models.CharField(default=1, max_length=50)),
                ('service6', models.CharField(default=1, max_length=50)),
                ('service7', models.CharField(default=1, max_length=50)),
                ('service8', models.CharField(default=1, max_length=50)),
            ],
        ),
    ]