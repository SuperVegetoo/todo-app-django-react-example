# Generated by Django 3.1.2 on 2020-10-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201015_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
