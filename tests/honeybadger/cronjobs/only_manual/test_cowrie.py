# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.

from unittest import TestCase

from honeybadger.cronjobs import cowrie
from honeybadger.models import IOC


class CowrieTestCase(TestCase):
    def test_sensors(self, *args, **kwargs):
        a = cowrie.ExtractCowrie()
        a.execute()
        self.assertTrue(a.success)
        iocs = IOC.objects.filter(cowrie=True)
        self.assertTrue(iocs)
