# Generated by Django 3.2.19 on 2023-06-14 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('order placed', 'order place'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'), ('cancel', 'cancel')], default='order placed', max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
