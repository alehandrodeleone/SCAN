# Generated by Django 4.2.5 on 2023-09-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_info_user_mb_ram_memory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_user',
            name='work_videocard',
            field=models.IntegerField(null=True),
        ),
    ]
