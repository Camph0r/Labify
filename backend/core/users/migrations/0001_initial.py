# Generated by Django 5.0.1 on 2024-01-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('rollnum', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], max_length=20)),
                ('groups', models.ManyToManyField(related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
