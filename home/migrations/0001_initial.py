
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('question1', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
                ('option4', models.CharField(max_length=30)),
                ('answer1', models.CharField(max_length=30)),
                ('question2', models.CharField(max_length=300)),
                ('option5', models.CharField(max_length=30)),
                ('option6', models.CharField(max_length=30)),
                ('option7', models.CharField(max_length=30)),
                ('option8', models.CharField(max_length=30)),
                ('answer2', models.CharField(max_length=30)),
            ],
        ),
    ]
