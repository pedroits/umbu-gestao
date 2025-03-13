# Generated by Django 5.1.7 on 2025-03-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=150)),
                ('neighborhood', models.CharField(max_length=150)),
                ('city_name', models.CharField(max_length=150)),
                ('house_number', models.CharField(max_length=10)),
                ('street_zipcode', models.CharField(max_length=20, null=True)),
                ('complement', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
