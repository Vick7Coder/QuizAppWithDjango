

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_quiz_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(default='1', help_text='Duration of the quiz in seconds'),
        ),
    ]
