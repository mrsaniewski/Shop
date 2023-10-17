# Generated by Django 3.2 on 2023-10-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('product_id', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]