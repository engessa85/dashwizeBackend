# Generated by Django 4.2.4 on 2023-09-15 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dataentery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual1",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual10",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual11",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual12",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual2",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual3",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual4",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual5",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual6",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual7",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual8",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebitactual9",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget1",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget10",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget11",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget12",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget2",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget3",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget4",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget5",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget6",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget7",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget8",
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="mtom",
            name="ebittarget9",
            field=models.IntegerField(default=100),
        ),
        migrations.CreateModel(
            name="ProfitLoss",
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
                ("revenue", models.IntegerField(default=100)),
                ("cost_of_good_sold", models.IntegerField(default=100)),
                ("sales", models.IntegerField(default=100)),
                ("marketing", models.IntegerField(default=100)),
                ("general_and_admin", models.IntegerField(default=100)),
                ("other_income", models.IntegerField(default=100)),
                ("other_expenses", models.IntegerField(default=100)),
                ("interest_and_tax", models.IntegerField(default=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
