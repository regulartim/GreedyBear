# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.
from dataclasses import dataclass


@dataclass
class Honeypot:
    name: str
    description: str = ""
