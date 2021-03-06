# Generated by Django 3.1 on 2020-08-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobClass",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jobcode", models.IntegerField(default=0)),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=400)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Socs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("detailedOccupation", models.IntegerField(unique=True)),
                ("detailName", models.CharField(max_length=400)),
                ("majorGroup", models.CharField(max_length=7)),
                ("minorGroup", models.CharField(max_length=7)),
                ("broadGroup", models.CharField(max_length=7)),
                ("majorName", models.CharField(max_length=200)),
                ("minorName", models.CharField(max_length=200)),
                ("broadName", models.CharField(max_length=200)),
            ],
        ),
    ]
