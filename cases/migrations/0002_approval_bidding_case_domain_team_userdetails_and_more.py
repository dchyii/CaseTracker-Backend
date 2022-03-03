# Generated by Django 4.0.3 on 2022-03-02 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('typeA', 'Type A'), ('typeB', 'Type B'), ('typeC', 'Type C')], max_length=20)),
                ('planned_completion_date', models.DateField()),
                ('submitted_date', models.DateField()),
                ('vetted_date', models.DateField()),
                ('supported_date', models.DateField()),
                ('supported2_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('supporter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_supporter1', to=settings.AUTH_USER_MODEL)),
                ('supporter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_supporter2', to=settings.AUTH_USER_MODEL)),
                ('vetter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_vetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('typeL', 'Type L'), ('typeD', 'Type D'), ('typeO', 'Type O')], max_length=20)),
                ('planned_completion_date', models.DateField()),
                ('submitted_date', models.DateField()),
                ('vetted_date', models.DateField()),
                ('supported_date', models.DateField()),
                ('supported2_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('supporter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidding_supporter1', to=settings.AUTH_USER_MODEL)),
                ('supporter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidding_supporter2', to=settings.AUTH_USER_MODEL)),
                ('vetter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidding_vetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('value', models.PositiveIntegerField()),
                ('current_status', models.CharField(choices=[('planning', 'Planning'), ('bidding', 'Bidding'), ('approval', 'Approval'), ('contracting', 'Contracting')], max_length=20)),
                ('current_step', models.CharField(choices=[('drafting', 'Drafting'), ('vetting', 'Vetting'), ('clearance1', 'Clearance 1'), ('clearance2', 'Clearance 2'), ('pending approval', 'Pending Approval')], max_length=20)),
                ('next_step', models.CharField(choices=[('drafting', 'Drafting'), ('vetting', 'Vetting'), ('clearance1', 'Clearance 1'), ('clearance2', 'Clearance 2'), ('pending approval', 'Pending Approval')], max_length=20)),
                ('approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.approval')),
                ('bidding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.bidding')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('services', 'Services'), ('infocomm tech', 'Infocomm Tech'), ('general goods', 'General Goods')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_staffer', to=settings.AUTH_USER_MODEL)),
                ('supporter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_supporter1', to=settings.AUTH_USER_MODEL)),
                ('supporter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_supporter2', to=settings.AUTH_USER_MODEL)),
                ('vetter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_vetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.appointment')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.domain')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('typeL', 'Type L'), ('typeD', 'Type D')], max_length=20)),
                ('planned_completion_date', models.DateField()),
                ('submitted_date', models.DateField()),
                ('vetted_date', models.DateField()),
                ('supported_date', models.DateField()),
                ('supported2_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('supporter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning_supporter1', to=settings.AUTH_USER_MODEL)),
                ('supporter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning_supporter2', to=settings.AUTH_USER_MODEL)),
                ('vetter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning_vetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contracting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('manager', 'Manager'), ('deputy director', 'Deputy Director'), ('director', 'Director')], max_length=20)),
                ('planned_completion_date', models.DateField()),
                ('submitted_date', models.DateField()),
                ('vetted_date', models.DateField()),
                ('supported_date', models.DateField()),
                ('supported2_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('supporter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_supporter1', to=settings.AUTH_USER_MODEL)),
                ('supporter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_supporter2', to=settings.AUTH_USER_MODEL)),
                ('vetter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_vetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('comment', models.CharField(max_length=200)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='contracting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.contracting'),
        ),
        migrations.AddField(
            model_name='case',
            name='current_step_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_step_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='next_step_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_step_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='planning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.planning'),
        ),
        migrations.AddField(
            model_name='case',
            name='staffer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_staffer', to=settings.AUTH_USER_MODEL),
        ),
    ]