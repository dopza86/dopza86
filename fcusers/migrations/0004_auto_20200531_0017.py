# Generated by Django 3.0.6 on 2020-05-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcusers', '0003_auto_20200529_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcusers',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스트캠퍼스 사용자'},
        ),
        migrations.AddField(
            model_name='fcusers',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
