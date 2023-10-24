from django.core.management.base import BaseCommand
from url_shortener.models import URLShortener

class Command(BaseCommand):
    help = 'Clear all objects from URLShortener model'
    def handle(self, *args, **options):
        URLShortener.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All objects from URLShortener model have been deleted.'))
