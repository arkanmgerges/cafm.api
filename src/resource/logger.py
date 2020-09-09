from logging import Logger

import src.resource.AppDi as AppDi

logger = AppDi.instance.get(Logger)
