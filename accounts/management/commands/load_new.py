from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User

from accounts.models import Price, WorkType

class Command(BaseCommand):
	help = "This command to load default domain and subdomains samples into database"
	def add_arguments(self, parser):
		parser.add_argument("--add", action="store_true", dest="add", default=True, help="add default domain only")
	def handle(self, *args, **options):
		if options["add"]:
			user1, created = User.objects.get_or_create(pk=1)#daha önce kaydetmisse bidaha kaydetmesin
			if created:
				user1.username = "admin"
				user1.first_name = "İlayda"
				user1.last_name = "AkBulut"
				user1.email = "admin@example.com"
				user1.set_password("1")
				user1.is_active = True
				user1.is_staff = True
				user1.is_superuser = True
				user1.save()
				print("Default User Added")
			price1, created = Price.objects.get_or_create(pk=1)
			if created:
				price1.name = "Çınar Restoran"
				price1.expense = 20
				price1.save()
				print("Default Price 1 Added")
			price2, created = Price.objects.get_or_create(pk=2)
			if created:
				price2.name = "Üniversite Yemekhanesi"
				price2.expense = 15
				price2.save()
				print("Default Price 2 Added")
			price3, created = Price.objects.get_or_create(pk=3)
			if created:
				price3.name = "Yemek Ücret"
				price3.expense = 10
				price3.save()
				print("Default Price 3 Added")
			work1, created = WorkType.objects.get_or_create(pk=1)
			if work1:
				work1.name = "Stajyer"
				work1.save()
				print("Default WorkType 1 Added")
			work2, created = WorkType.objects.get_or_create(pk=2)
			if work2:
				work2.name = "Çalışan"
				work2.save()
				print("Default WorkType 2 Added")