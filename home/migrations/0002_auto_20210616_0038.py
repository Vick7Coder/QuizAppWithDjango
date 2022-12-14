

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answer3',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer5',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option10',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option11',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option12',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option13',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option14',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option15',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option16',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option17',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option18',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option19',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option20',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option9',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question3',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question4',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question5',
            field=models.CharField(default='', max_length=300),
        ),
    ]
