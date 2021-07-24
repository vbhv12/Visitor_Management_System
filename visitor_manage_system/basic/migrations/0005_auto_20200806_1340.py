# Generated by Django 3.0.8 on 2020-08-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20200730_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='age',
            field=models.IntegerField(default=21),
        ),
        migrations.AddField(
            model_name='host',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Female', max_length=10),
        ),
        migrations.AddField(
            model_name='visitor',
            name='age',
            field=models.IntegerField(default=21),
        ),
        migrations.AddField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Female', max_length=10),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(default=' ', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('organizer', 'event_date_time')},
        ),
    ]