

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210626_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='image',
        ),
    ]
