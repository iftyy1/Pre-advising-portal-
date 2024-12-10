# Generated by Django 5.1.1 on 2024-09-16 22:37

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("dept_initial", models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("initial", models.CharField(max_length=3, unique=True)),
                ("advising_access", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panel.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Faculty",
                "verbose_name_plural": "Faculty",
                "ordering": ["initial"],
            },
            bases=("panel.customuser",),
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff",
                "verbose_name_plural": "Staff",
                "ordering": ["first_name", "last_name"],
            },
            bases=("panel.customuser",),
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_name", models.CharField(max_length=70)),
                ("course_code", models.CharField(max_length=7)),
                (
                    "prerequisite_course",
                    models.TextField(blank=True, max_length=70, null=True),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panel.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(null=True)),
                ("theory_room", models.CharField(max_length=10, null=True)),
                ("lab_room", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "class_time",
                    models.CharField(
                        choices=[
                            ("0800_to_0920", "08.00 am - 9.20 am"),
                            ("0930_to_1050", "09.30 am - 10.50 am"),
                            ("1100_to_1220", "11.00 am - 12.20 pm"),
                            ("1230_to_0150", "12.30 pm - 01.50 pm"),
                            ("0200_to_0320", "02.00 pm - 03.20 pm"),
                            ("0330_to_0450", "03.30 pm - 04.50 pm"),
                            ("0500_to_0620", "05.00 pm - 06.20 pm"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "exam_time",
                    models.CharField(
                        choices=[
                            ("0800_to_0920", "08.00 am - 9.20 am"),
                            ("0930_to_1050", "09.30 am - 10.50 am"),
                            ("1100_to_1220", "11.00 am - 12.20 pm"),
                            ("1230_to_0150", "12.30 pm - 01.50 pm"),
                            ("0200_to_0320", "02.00 pm - 03.20 pm"),
                            ("0330_to_0450", "03.30 pm - 04.50 pm"),
                            ("0500_to_0620", "05.00 pm - 06.20 pm"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "class_day",
                    models.CharField(
                        choices=[
                            ("sat_thu", "Saturday - Thursday"),
                            ("sun_tue", "Sunday - Tuesday"),
                            ("mon_wed", "Monday - Wednesday"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "lab_day",
                    models.CharField(
                        choices=[
                            ("sat", "Saturday"),
                            ("sun", "Sunday"),
                            ("mon", "Monday"),
                            ("tue", "Tuesday"),
                            ("wed", "Wednesday"),
                            ("thu", "Thursday"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("total_seat", models.IntegerField(default=40)),
                ("seat_booked", models.IntegerField(default=0)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="panel.course"
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panel.department",
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="panel.faculty"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("student_id", models.PositiveBigIntegerField(unique=True)),
                ("credits_completed", models.IntegerField(default=0)),
                (
                    "cgpa",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[
                            django.core.validators.MaxValueValidator(4),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                ("advising_access", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panel.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "ordering": ["student_id"],
            },
            bases=("panel.customuser",),
        ),
    ]