import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','vj.settings')

import django
django.setup()

import random
from user_account.models import Account
from faker import Faker 

fakegen = Faker()
'''
def add_gender():
	g = Account.objects.get_or_create(gender=random.choice(gender))[0]
	g.save()
	return g
'''

def populate(N=5):

	for entry in range(N):
		gender=['male','female']

		#gender=add_gender()
		gender=random.choice(gender)

		fake_lastname= fakegen.last_name()
		fake_firstname = fakegen.first_name()
		fake_email = fakegen.email()


		acc= Account.objects.get_or_create(firstname=fake_firstname,lastname=fake_lastname,email=fake_email,gender=gender)[0]

if __name__ == '__main__':
	print("populating script")
	populate(20)
	print("Done")