# Generated by Django 5.1.3 on 2024-11-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_customuser_is_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_activate',
            field=models.BooleanField(db_default=False),
        ),
    ]