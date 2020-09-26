"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from logging import Logger

import src.resource.Di as Di

logger = Di.instance.get(Logger)
