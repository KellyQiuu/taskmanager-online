# Generated by Django 3.2.6 on 2023-07-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('RTR', 'RTR'), ('PTP', 'PTP'), ('CI', 'CI'), ('IC', 'IC'), ('TE', 'TE'), ('IT', 'IT'), ('support team', 'support team')], max_length=50),
        ),
    ]
