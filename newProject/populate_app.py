import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project.settings')
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import django
import random
from new_app.models import AccessRecord, Webpage, Topic
from faker import Faker

django.setup()

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get topic for entry
        top = add_topic()

        # Create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new webpage entry

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        # print(acc_rec.date) # objects.all().values_list('id', 'name')
        # print(fake_date)


if __name__ == '__main__':
    print('populating script!')
    populate(1)
    print('Complete')
