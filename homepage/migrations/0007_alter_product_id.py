# Generated by Django 4.2.5 on 2023-10-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homepage", "0006_alter_user_options_alter_user_groups_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
