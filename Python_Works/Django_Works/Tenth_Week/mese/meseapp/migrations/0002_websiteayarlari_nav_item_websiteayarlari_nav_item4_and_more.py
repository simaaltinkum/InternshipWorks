# Generated by Django 4.2.3 on 2023-08-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item4',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item5',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item6',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item_2',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='websiteayarlari',
            name='nav_item_3',
            field=models.CharField(default=1, max_length=50),
        ),
    ]