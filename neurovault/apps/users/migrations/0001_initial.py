# Generated by Django 4.0.6 on 2022-09-27 21:44

from django.db import migrations
from django.conf import settings

def create_default_app(apps, schema_editor):
    Application = apps.get_registered_model('oauth2_provider', 'Application') 
    Application.objects.get_or_create(
        name=settings.DEFAULT_OAUTH_APP_NAME,
        redirect_uris=['http://localhost'],
        pk=settings.DEFAULT_OAUTH_APPLICATION_ID
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_default_app),
    ]
