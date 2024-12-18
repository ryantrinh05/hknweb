# Generated by Django 4.2.16 on 2024-12-07 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "studentservices",
            "0013_rename_required_courseguideadjacencylist_target_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courseguideadjacencylist",
            name="type",
        ),
        migrations.AddField(
            model_name="courseguideadjacencylist",
            name="recommended",
            field=models.ManyToManyField(
                related_name="adjacency_list_recommended",
                to="studentservices.courseguidenode",
            ),
        ),
    ]
