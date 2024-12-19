from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Retroactively refetch measurements for Trac metrics."
    label = "slug"

    def handle(self, **kwargs):
        print(f"{settings.DEBUG=}")
