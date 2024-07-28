# Generated by Django 5.0.7 on 2024-07-27 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_orderline_received_alter_order_order_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderLog",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("message", models.TextField(verbose_name="Message")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="orders.order",
                        verbose_name="Order",
                    ),
                ),
            ],
        ),
    ]
