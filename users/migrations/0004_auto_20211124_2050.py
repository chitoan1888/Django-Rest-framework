# Generated by Django 3.2.9 on 2021-11-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_is_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uid',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]