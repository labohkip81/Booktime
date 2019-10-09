from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import Products in BookTime'

    def handle(self, *args, **options):
        self.stdout.write("Importing Data.")