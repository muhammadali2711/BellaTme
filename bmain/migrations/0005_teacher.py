# Generated by Django 4.1.4 on 2022-12-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmain', '0004_rating_alter_course_options_alter_why_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.JSONField(default={'chi': '', 'de': '', 'en': '', 'ja': '', 'ru': '', 'uz': '', 'zn': ''})),
                ('img', models.ImageField(upload_to='teachers')),
            ],
            options={
                'verbose_name': 'Teacher',
            },
        ),
    ]