from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@tosya.ru',
            first_name='tosik',
            last_name='tosevich',
            is_staff=True,
            is_superuser=True,
            is_active=True

        )

        user.set_password('123qwe345rty')
        user.save()