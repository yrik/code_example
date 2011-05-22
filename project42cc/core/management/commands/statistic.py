from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    args = ''
    help = 'List of models and items in each models'

    def handle(self, *args, **options):
        for model in models.get_models():
            msg = ('Model "%s" - %d items\n' %
                         (model, model.objects.count()))
            self.stdout.write(msg)
            self.stderr.write('error: ' + msg)
