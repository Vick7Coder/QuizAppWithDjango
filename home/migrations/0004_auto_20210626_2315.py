

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210626_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question1',
        ),
    ]
