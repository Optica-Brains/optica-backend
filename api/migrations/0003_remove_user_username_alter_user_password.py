# Generated by Django 4.0.3 on 2022-04-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_branch_id_order_branch_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
