# Generated by Django 3.2.6 on 2023-07-23 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=128)),
                ('english_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('gid', models.CharField(max_length=50)),
                ('grade', models.SmallIntegerField()),
                ('title', models.CharField(max_length=128)),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('manager', models.CharField(max_length=128)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('current_stage', models.CharField(choices=[('Planning', 'Planing'), ('Started', 'Started'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Approved', 'Approved'), ('Completed', 'Completed')], max_length=55)),
                ('time_occupancy', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.employee')),
            ],
        ),
    ]