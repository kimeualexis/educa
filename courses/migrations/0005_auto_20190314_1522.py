# Generated by Django 2.1.7 on 2019-03-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.FileField(upload_to='courses'),
        ),
    ]
