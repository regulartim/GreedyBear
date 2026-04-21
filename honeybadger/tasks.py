# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.
from __future__ import absolute_import, unicode_literals

from celery import chain, shared_task
from honeybadger.settings import CLUSTER_COWRIE_COMMAND_SEQUENCES


@shared_task()
def extract_log4pot():
    from honeybadger.cronjobs.log4pot import ExtractLog4Pot

    ExtractLog4Pot().execute()


@shared_task()
def extract_cowrie():
    from honeybadger.cronjobs.cowrie import ExtractCowrie

    ExtractCowrie().execute()


# FEEDS
@shared_task()
def extract_general():
    from honeybadger.cronjobs.general import ExtractAllGenerals

    ExtractAllGenerals().execute()


@shared_task()
def extract_sensors():
    from honeybadger.cronjobs.sensors import ExtractSensors

    ExtractSensors().execute()


@shared_task()
def monitor_honeypots():
    from honeybadger.cronjobs.monitor_honeypots import MonitorHoneypots

    MonitorHoneypots().execute()


@shared_task()
def monitor_logs():
    from honeybadger.cronjobs.monitor_logs import MonitorLogs

    MonitorLogs().execute()


# SCORING
@shared_task()
def chain_train_and_update():
    from honeybadger.cronjobs.scoring.scoring_jobs import TrainModels, UpdateScores

    trainer = TrainModels()
    trainer.execute()

    updater = UpdateScores()
    updater.data = trainer.current_data
    updater.execute()


# COMMANDS
@shared_task()
def cluster_commands():
    from honeybadger.cronjobs.commands.cluster import ClusterCommandSequences

    if CLUSTER_COWRIE_COMMAND_SEQUENCES:
        ClusterCommandSequences().execute()


# CLEAN UP
@shared_task()
def clean_up_db():
    from honeybadger.cronjobs.cleanup import CleanUp

    CleanUp().execute()
