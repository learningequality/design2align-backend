# Generated by Django 2.2.6 on 2019-10-10 02:07

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(help_text='A unique identifier for the source document', max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('country', models.CharField(help_text='Country', max_length=200)),
                ('digitization_method', models.CharField(choices=[('manual_entry', 'Manual data entry'), ('scan_manual', 'Curriculum manually extracted from OCR'), ('automated_scan', 'Automated stucture extraction via OCR'), ('website_scrape', 'Curriculum scraped from website'), ('data_import', 'Curriculum imported from data')], help_text='Digitization method', max_length=200)),
                ('source_url', models.CharField(blank=True, help_text='URL of source used for this document', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=True, help_text='True for draft version of the curriculum data.')),
            ],
        ),
        migrations.CreateModel(
            name='DataExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exportdirname', models.CharField(blank=True, max_length=400, null=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineLearningModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('model_version', models.IntegerField()),
                ('git_hash', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, unique=True)),
                ('value', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StandardNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('identifier', models.CharField(max_length=300)),
                ('kind', models.CharField(max_length=100)),
                ('title', models.TextField(help_text='Primary text that represents this node.')),
                ('sort_order', models.FloatField(default=1.0)),
                ('time_units', models.FloatField(blank=True, help_text='A numeric value ~= to the # hours of instruction for this unit or topic', null=True)),
                ('notes', models.TextField(blank=True, help_text='Additional notes, description, and supporting text from the source.')),
                ('extra_fields', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='alignmentapp.CurriculumDocument')),
            ],
        ),
        migrations.CreateModel(
            name='HumanRelevanceJudgment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('confidence', models.FloatField(blank=True, null=True)),
                ('extra_fields', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('mode', models.CharField(max_length=30)),
                ('ui_name', models.CharField(max_length=100)),
                ('ui_version_hash', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_test_data', models.BooleanField(blank=True, help_text='True for held out test data.', null=True)),
                ('node1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node1+', to='alignmentapp.StandardNode')),
                ('node2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node2+', to='alignmentapp.StandardNode')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='judgments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='standardnode',
            constraint=models.UniqueConstraint(condition=models.Q(depth=1), fields=('document', 'depth'), name='single_root_per_document'),
        ),
    ]