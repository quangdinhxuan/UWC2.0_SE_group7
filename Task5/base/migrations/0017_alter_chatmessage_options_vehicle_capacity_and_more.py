# Generated by Django 4.1.3 on 2022-11-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_mcp_collector_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-updated', 'created']},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='capacity',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_cons',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='weight',
            field=models.TextField(default='Unknown'),
        ),
    ]
