# Generated by Django 4.2.1 on 2023-06-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redforceapp', '0003_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]