# Generated by Django 5.2.4 on 2025-07-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0006_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
