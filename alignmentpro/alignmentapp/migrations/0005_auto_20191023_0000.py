##################################################
# MIT License
#
# Copyright (c) 2019 Learning Equality
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
##################################################

# Generated by Django 2.2.6 on 2019-10-23 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alignmentapp', '0004_auto_20191013_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('section_zip', models.FileField(blank=True, null=True, upload_to='')),
                ('num_chunks', models.IntegerField()),
                ('text', models.TextField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='alignmentapp.CurriculumDocument')),
            ],
        ),
        migrations.DeleteModel(
            name='MachineLearningModel',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.CharField(choices=[('instructional_designer', 'Instructional Designer'), ('curriculum', 'Curriculum Alignment Expert'), ('content_expert', 'OER Expert'), ('teacher', 'Teacher/Coach'), ('designer', 'Designer or Frontend Developer'), ('developer', 'Technologist and/or Developer'), ('data_science', 'Machine Learning and Data Science'), ('metadata', 'Metadata'), ('other', 'Other')], help_text='What is your background experience?', max_length=50),
        ),
        migrations.AddConstraint(
            model_name='documentsection',
            constraint=models.UniqueConstraint(condition=models.Q(depth=1), fields=('document', 'depth'), name='document_section_single_root'),
        ),
    ]
