# Generated by Django 4.0 on 2021-12-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
