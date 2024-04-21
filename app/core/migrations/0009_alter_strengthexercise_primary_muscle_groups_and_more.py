# Generated by Django 5.0.4 on 2024-04-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_musclegroup_strengthexercise_primary_muscle_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strengthexercise',
            name='primary_muscle_groups',
            field=models.ManyToManyField(related_name='primary_muscle_groups', to='core.musclegroup'),
        ),
        migrations.AlterField(
            model_name='strengthexercise',
            name='secondary_muscle_groups',
            field=models.ManyToManyField(related_name='secondary_muscle_groups', to='core.musclegroup'),
        ),
    ]
