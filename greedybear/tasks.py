from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task()
def extract_attacks():
    from greedybear.cronjobs.cowrie import ExtractCowrie
    from greedybear.cronjobs.log4pot import ExtractLog4Pot

    ExtractLog4Pot().execute()
    ExtractCowrie().execute()


@shared_task()
def extract_sensors():
    from greedybear.cronjobs.sensors import ExtractSensors

    ExtractSensors().execute()