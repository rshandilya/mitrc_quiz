# Generated by Django 2.0.7 on 2018-08-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180822_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='obtained_marks',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]
