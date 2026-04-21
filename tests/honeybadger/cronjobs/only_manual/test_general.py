# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.

from unittest import TestCase

from django.db.models import Q
from honeybadger.cronjobs import general
from honeybadger.models import IOC

# FEEDS


class GeneralTestCase(TestCase):
    def test_sensors(self, *args, **kwargs):
        a = general.ExtractAllGenerals()
        a.execute()
        self.assertTrue(a.success)

        iocs = []
        for hp in ["heralding", "ciscoasa"]:
            iocs.extend(IOC.objects.filter(Q(general_honeypot__name__iexact=hp)))
        self.assertTrue(iocs)

        ciscoasa = general.ExtractGeneral(general.Honeypot("Ciscoasa"))
        ciscoasa.execute()
        glutton = general.ExtractGeneral(general.Honeypot("Glutton"))
        glutton.execute()
        assert ciscoasa.first_time_run != glutton.first_time_run
