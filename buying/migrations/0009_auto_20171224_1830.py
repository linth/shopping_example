# Generated by Django 2.0 on 2017-12-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0008_auto_20171224_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderall',
            name='order_id_number',
            field=models.CharField(default='26234908CA', max_length=256, primary_key=True, serialize=False),
        ),
    ]
