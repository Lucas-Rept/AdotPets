# Generated by Django 4.2.7 on 2023-11-03 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_user', '0002_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=250)),
                ('value', models.CharField(default=0, max_length=6)),
                ('category', models.CharField(max_length=50)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('fk_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='auth_user.company')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='product_image')),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='store.product')),
            ],
        ),
    ]