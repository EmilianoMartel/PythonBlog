# Generated by Django 4.0.6 on 2022-08-09 21:21


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_contenido_remove_user_favs_user_mail_user_fav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('P', 'Película'), ('S', 'Serie'), ('C', 'Corto')], max_length=1)),
                ('body', models.TextField(null=True)),
                ('puntaje', models.FloatField()),
                ('film', models.ManyToManyField(to='products.contenido')),

            ],
        ),
    ]
