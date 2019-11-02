# Generated by Django 2.2.6 on 2019-11-02 21:54

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('ins_dt', models.DateTimeField(auto_now_add=True)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('use_tf', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'db_table': 'post_post',
                'ordering': ['-ins_dt'],
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
