# Generated by Django 5.0.2 on 2024-02-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_remove_doctors_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='about_doctor',
            field=models.TextField(max_length=1000, verbose_name='Doktor haqida malumot'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='about_doctor_rus',
            field=models.TextField(max_length=1000, verbose_name='Doktor haqida malumot rus tilida'),
        ),
    ]
