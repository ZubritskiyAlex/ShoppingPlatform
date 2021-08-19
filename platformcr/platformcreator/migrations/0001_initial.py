# Generated by Django 3.2.6 on 2021-08-18 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=30, verbose_name='username')),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Photo')),
                ('date_created', models.DateField(auto_now=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of category')),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(blank=True, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Store name')),
                ('url', models.URLField(blank=True, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/images', verbose_name='Image')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='platformcreator.category', verbose_name='Category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'db_table': 'Store',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Price')),
                ('date_created', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/images', verbose_name='Image')),
                ('url', models.URLField(blank=True, null=True, unique=True, verbose_name='URL')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='platformcreator.category', verbose_name='Category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_products', to=settings.AUTH_USER_MODEL)),
                ('stores', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='platformcreator.store', verbose_name='Stores')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Product',
            },
        ),
    ]
