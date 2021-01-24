# Generated by Django 3.1.5 on 2021-01-23 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Section',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='test',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='CourseDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=200)),
                ('time', models.TimeField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.course')),
            ],
        ),
    ]
