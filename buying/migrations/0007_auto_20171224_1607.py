# Generated by Django 2.0 on 2017-12-24 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0006_auto_20171224_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderall',
            name='order_id_number',
            field=models.CharField(default='24001B3202', max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='orderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buying.Order'),
        ),
    ]