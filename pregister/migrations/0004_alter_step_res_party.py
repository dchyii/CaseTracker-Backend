# Generated by Django 4.0.3 on 2022-03-08 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pregister', '0003_alter_step_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='res_party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='res_party_steps', to=settings.AUTH_USER_MODEL),
        ),
    ]
