# Generated by Django 4.0 on 2021-12-16 04:19

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
                ('second', models.FloatField()),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
