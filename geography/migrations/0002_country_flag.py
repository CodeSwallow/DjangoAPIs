# Generated by Django 4.0.4 on 2022-04-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]