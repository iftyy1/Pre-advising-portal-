# Generated by Django 5.1.1 on 2024-09-23 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0008_remove_studentenrollment_enrollment_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faculty",
            name="advising_access",
        ),
        migrations.RemoveField(
            model_name="student",
            name="advising_access",
        ),
    ]