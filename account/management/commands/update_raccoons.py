# -*- coding: utf-8 -*-
"""
Creates users in DB from JSON file
"""

import json
from django.core.management.base import BaseCommand, CommandError
from account.models import Account


class Command(BaseCommand):
    """
    Command that creates users from json file.
    """
    help = "Create users from json file"

    def add_arguments(self, parser):
        parser.add_argument('json_path', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        Used to create users from json fixture.
        Expected data:
        {
            raccoons:
              [
                 {
                    "email": "example.com",
                    "first_name": "user_first_name",
                    "last_name": "user_last_name",
                 },
                 ...
              ]
        }
        """
        try:
            with open(options['json_path'][0], 'r') as json_dump:
                data = json.load(json_dump)
        except IOError:
            raise CommandError("Cannot open file `{}`".format(options['json_path']))

        for item in data['raccoons']:
            user, created = Account.objects.get_or_create(email=item['email'])
            if created:
                user.first_name = item['first_name']
                user.last_name = item['last_name']
                user.username = "%s%s" % (item['first_name'], item['last_name'])
                user.save()
                msg = (
                    "Successfully created user with email {}, first name - {}, last name {}"
                ).format(
                    user.email,
                    item['first_name'],
                    item['last_name']
                )
                self.stdout.write(msg)
