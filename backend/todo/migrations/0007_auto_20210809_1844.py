# Generated by Django 3.2.5 on 2021-08-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hourly', models.IntegerField()),
                ('totalHours', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
