# Generated by Django 4.0.3 on 2022-06-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_appointment_appointdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointdata',
            field=models.CharField(max_length=40),
        ),
    ]