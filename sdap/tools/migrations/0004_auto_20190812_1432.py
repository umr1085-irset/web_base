# Generated by Django 2.0.13 on 2019-08-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20190807_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.RenameField(
            model_name='tool',
            old_name='html_name',
            new_name='link',
        ),
        migrations.AddField(
            model_name='tool',
            name='icon',
            field=models.ImageField(null=True, upload_to='tools/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='tool',
            name='type',
            field=models.CharField(choices=[('LOCAL', 'Local link'), ('COMPUTED', 'Local job'), ('REMOTE', 'Remote tool')], default='LOCAL', max_length=20),
        ),
        migrations.AlterField(
            model_name='tool',
            name='command_line',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='form_name',
            field=models.CharField(blank=True, default='default_form', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='path',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='script_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='short_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='tool',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_of', to='tools.Category'),
            preserve_default=False,
        ),
    ]