# Generated by Django 2.2.1 on 2019-06-05 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('check', models.BooleanField(default=False)),
                ('date_to_do', models.DateField(blank=True, default='2019-05-26', null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
        ),
    ]