# Generated by Django 4.2.1 on 2023-06-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redforceapp', '0008_alter_customuser_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='subscribe',
            field=models.CharField(choices=[('not', 'not'), ('white', 'white'), ('green', 'green')], default='not', max_length=10),
        ),
    ]
