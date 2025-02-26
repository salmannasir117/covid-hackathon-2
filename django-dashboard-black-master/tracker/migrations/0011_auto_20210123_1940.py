# Generated by Django 2.2.10 on 2021-01-24 00:40

from django.db import migrations, models
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20210123_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedatetime',
            name='day',
            field=models.CharField(blank=True, choices=[(tracker.models.Day('Monday'), 'Monday'), (tracker.models.Day('Wednesday'), 'Wednesday')], max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='workplace',
            field=models.CharField(blank=True, choices=[(tracker.models.Building('760 Spring Street'), '760 Spring Street'), (tracker.models.Building('Clough Undergraduate Learning Commons'), 'Clough Undergraduate Learning Commons'), (tracker.models.Building('WEST vILLAGE DINING COMMONS'), 'WEST vILLAGE DINING COMMONS')], max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='dorm',
            field=models.CharField(blank=True, choices=[(tracker.models.Dorm('Armstrong'), 'Armstrong'), (tracker.models.Dorm('Brown'), 'Brown'), (tracker.models.Dorm('Cloudman'), 'Cloudman')], max_length=200),
        ),
    ]
