# Generated by Django 4.2.4 on 2023-09-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("students_courses", "0001_initial"),
        ("courses", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="my_courses",
            field=models.ManyToManyField(
                related_name="students",
                through="students_courses.StudentCourse",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="account",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
