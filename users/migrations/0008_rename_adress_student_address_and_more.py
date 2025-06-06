# Generated by Django 5.2.1 on 2025-05-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_medicalrecord_drinks_alcohol_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='drinks_alcohol',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='had_surgeries',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='has_heart_problems',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='has_joint_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='practices_physical_activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='smokes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='takes_medication',
            field=models.BooleanField(default=False),
        ),
    ]
