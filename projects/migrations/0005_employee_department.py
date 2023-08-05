# Generated by Django 3.2.6 on 2023-07-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_employeeprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('RTR', 'RTR'), ('PTP', 'PTP'), ('CI', 'CI'), ('IC', 'IC'), ('TE', 'TE'), ('IT', 'IT')], max_length=50, null=True),
        ),
    ]