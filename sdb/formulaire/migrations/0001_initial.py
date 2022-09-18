# Generated by Django 4.1 on 2022-08-23 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import formulaire.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enquete', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(blank=True, default='', null=True, upload_to=formulaire.models.upload_path)),
                ('elements', models.CharField(default='', max_length=9000)),
                ('sujets', models.CharField(default='', max_length=9000)),
                ('created', models.DateField(auto_now_add=True)),
                ('enquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulaires', to='enquete.enquete')),
                ('enqueteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulaires', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
