# Generated by Django 2.2.1 on 2019-05-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20190520_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateField(verbose_name='data published'),
        ),
    ]