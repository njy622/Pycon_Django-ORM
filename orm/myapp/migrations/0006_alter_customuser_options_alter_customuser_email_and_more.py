# Generated by Django 5.1.3 on 2024-11-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_customuser_is_activate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': '유저 목록'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_activate',
            field=models.BooleanField(db_default=True, default=True, verbose_name='활성 여부'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='사용자 이름'),
        ),
    ]