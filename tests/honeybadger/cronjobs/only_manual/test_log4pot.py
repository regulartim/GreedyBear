# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.

from unittest import TestCase

from honeybadger.cronjobs import log4pot
from honeybadger.models import IOC


class Log4PotTestCase(TestCase):
    def test_sensors(self, *args, **kwargs):
        a = log4pot.ExtractLog4Pot()
        a.execute()
        self.assertTrue(a.success)
        iocs = IOC.objects.filter(log4j=True)
        self.assertTrue(iocs)
