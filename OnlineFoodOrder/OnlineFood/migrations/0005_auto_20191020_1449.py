# Generated by Django 2.2.6 on 2019-10-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFood', '0004_auto_20191020_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addnewcustomer',
            name='customer_contact_number',
            field=models.DecimalField(decimal_places=2, max_digits=12, primary_key=True, serialize=False),
        ),
    ]