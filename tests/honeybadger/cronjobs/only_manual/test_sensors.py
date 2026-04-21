# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.

from unittest import TestCase

from honeybadger.cronjobs import sensors
from honeybadger.models import Sensors


class SensorsTestCase(TestCase):
    def test_sensors(self, *args, **kwargs):
        s = sensors.ExtractSensors()
        s.execute()
        self.assertTrue(s.success)
        s_ob = Sensors.objects.all()
        self.assertTrue(s_ob)
