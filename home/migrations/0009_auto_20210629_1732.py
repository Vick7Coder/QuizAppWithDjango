

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_auto_20210627_1030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Result',
            new_name='Marks_Of_User',
        ),
    ]
