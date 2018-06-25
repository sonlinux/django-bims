# Generated by Django 2.0.6 on 2018-06-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0008_category_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv/')),
            ],
            options={
                'verbose_name': 'CSV Document',
                'verbose_name_plural': 'CSV Documents',
            },
        ),
    ]
