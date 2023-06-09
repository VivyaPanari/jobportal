# Generated by Django 4.2.3 on 2023-07-10 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0005_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('applicant_email', models.EmailField(max_length=254, verbose_name='Email ID')),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Under Review', 'Under Review'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Not Applied', max_length=20)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.employer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.job')),
            ],
        ),
    ]
