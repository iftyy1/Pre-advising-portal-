# Generated by Django 5.1.1 on 2024-09-23 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0007_studentenrollment_delete_studentsection"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentenrollment",
            name="enrollment_date",
        ),
    ]
