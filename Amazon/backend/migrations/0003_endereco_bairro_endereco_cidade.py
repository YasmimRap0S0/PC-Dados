# Generated by Django 5.0.8 on 2024-11-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]