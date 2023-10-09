import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project.settings')
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import django
import random
from users.models import Users
from faker import Faker

django.setup()

fakegen = Faker()


def populate(n=5):
    for entry in range(n):

        fake_name = fakegen.name()
        names = fake_name.split(' ')
        fake_email = fakegen.email()
        # print(names[0])
        # print(names[1])

        usr = Users.objects.get_or_create(first_name=names[0], last_name=names[1],user_email=fake_email)[0]


if __name__ == '__main__':
    print('populating users!')
    populate(10)
    print('Complete')
