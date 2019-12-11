# Generated by Django 3.0 on 2019-12-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('cartao', models.IntegerField()),
                ('pagamento', models.CharField(choices=[('AV', 'Pagamento à vista'), ('P2', 'Parcelado em 2x'), ('P3', 'Parcelado em 3x')], max_length=2)),
            ],
        ),
    ]
