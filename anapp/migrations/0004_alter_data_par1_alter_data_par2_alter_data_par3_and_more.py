# Generated by Django 4.0.5 on 2022-07-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anapp', '0003_alter_data_par1_alter_data_par2_alter_data_par3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='par1',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='par2',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='par3',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='par4',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='par5',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]