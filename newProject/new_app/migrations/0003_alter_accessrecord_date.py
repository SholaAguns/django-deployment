# Generated by Django 4.2.5 on 2023-10-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_accessrecord_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
