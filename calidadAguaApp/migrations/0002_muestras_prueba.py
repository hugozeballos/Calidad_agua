# Generated by Django 4.2.7 on 2023-11-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calidadAguaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muestras',
            name='prueba',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]