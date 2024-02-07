# Generated by Django 4.2.10 on 2024-02-07 13:39

from django.db import migrations, models
import fillers.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutUsContextModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "main_image_upper",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Первая большая картинка",
                    ),
                ),
                (
                    "main_image_down",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Вторая большая картинка",
                    ),
                ),
                (
                    "small_image_left_first",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Первая картинка левого столбика",
                    ),
                ),
                (
                    "small_image_right_first",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Первая картинка правого столбика",
                    ),
                ),
                (
                    "small_image_left_second",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Вторая картинка левого столбика",
                    ),
                ),
                (
                    "small_image_right_second",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Вторая картинка правого столбика",
                    ),
                ),
                (
                    "small_image_left_third",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Третья картинка левого столбика",
                    ),
                ),
                (
                    "small_image_right_third",
                    models.ImageField(
                        null=True,
                        upload_to=fillers.models.user_directory_path,
                        verbose_name="Третья картинка правого столбика",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryDataModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
            ],
        ),
    ]
