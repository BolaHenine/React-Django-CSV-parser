# Generated by Django 3.2.5 on 2021-08-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210809_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='paycheck',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]