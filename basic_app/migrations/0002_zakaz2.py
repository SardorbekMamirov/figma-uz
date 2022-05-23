# Generated by Django 4.0.4 on 2022-05-23 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('poolframe', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='images/')),
                ('active', models.BooleanField(default=False)),
                ('count', models.PositiveIntegerField()),
                ('p_name', models.CharField(max_length=200)),
            ],
        ),
    ]
