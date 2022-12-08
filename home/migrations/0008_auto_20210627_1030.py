

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_answer_question_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='content',
        ),
    ]
