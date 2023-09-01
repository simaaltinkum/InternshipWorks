# Generated by Django 4.2.3 on 2023-08-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_users_email_remove_users_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='users',
            name='full_name',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
