# Generated by Django 4.0.3 on 2022-03-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregister', '0011_alter_case_approval_type_alter_case_need_by_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['stage', 'step']},
        ),
        migrations.AlterField(
            model_name='step',
            name='stage',
            field=models.CharField(choices=[('1. planning', 'Planning'), ('2. bidding', 'Bidding'), ('3. approval', 'Approval'), ('4. contracting', 'Contracting')], max_length=20),
        ),
        migrations.AlterField(
            model_name='step',
            name='step',
            field=models.CharField(choices=[('1. drafting', 'Drafting'), ('2. vetting', 'Vetting'), ('3. support1', 'Support1'), ('4. support2', 'Support2'), ('5. completed', 'Completed'), ('6. cancelled', 'Cancelled')], max_length=20),
        ),
    ]
