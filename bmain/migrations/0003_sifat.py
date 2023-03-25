# Generated by Django 4.1.4 on 2022-12-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmain', '0002_course_why_remove_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sifat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.JSONField(default={'chi': '', 'de': '', 'en': '', 'ja': '', 'ru': '', 'uz': '', 'zn': ''})),
                ('desc', models.JSONField(default={'chi': '', 'de': '', 'en': '', 'ja': '', 'ru': '', 'uz': '', 'zn': ''})),
                ('type', models.IntegerField(choices=[(1, 'For kids'), (2, 'For teens')], default=1)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
