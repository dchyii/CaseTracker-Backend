# Generated by Django 4.0.3 on 2022-03-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='type',
            field=models.CharField(default='l', max_length=1),
            preserve_default=False,
        ),
    ]
