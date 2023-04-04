from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    )
                ),
                (
                    'title', models.CharField(
                        max_length=200,
                        verbose_name='Название группы',
                    )
                ),
                (
                    'slug', models.SlugField(
                        max_length=100,
                        unique=True,
                        verbose_name='Уникальная часть адреса группы',
                    )
                ),
                (
                    'description', models.TextField(
                        verbose_name='Описание группы',
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    )
                ),
                (
                    'text', models.TextField(
                        verbose_name='Текст поста',
                    )
                ),
                (
                    'pub_date', models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата публикации поста',
                    )
                ),
                (
                    'author', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='posts',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Автор поста',
                    )
                ),
                (
                    'group', models.ForeignKey(
                        blank=True, null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='posts',
                        to='posts.Group',
                        verbose_name='Группа',
                    )
                ),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-pub_date',),
            },
        ),
    ]
