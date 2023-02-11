# Generated by Django 3.0.3 on 2020-05-15 16:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=1)),
                ('issue', models.IntegerField(default=1)),
                ('issue_title', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.CharField(max_length=500)),
                ('text', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('Unsubmitted', 'Unsubmitted'), ('Under Review', 'Peer Review'), ('Under Revision', 'Revision'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Typesetting', 'Typesetting'), ('pre_publication', 'Pre Publication'), ('Published', 'Published')], default='Unsubmitted', max_length=15)),
                ('published_at', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=300, unique=True)),
                ('j_image', models.ImageField(upload_to='j_images')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Journal Description')),
                ('keywords', models.ManyToManyField(blank=True, to='app.Keyword')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='EditorNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Editornotes', to='app.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Journal'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(related_name='keywords', to='app.Keyword'),
        ),
    ]