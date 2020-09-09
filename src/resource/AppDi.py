import logging
import os
from logging import Logger

from injector import Module, singleton, provider, Injector



class AppDi(Module):
    """
    Dependency injection module of the app

    """

    @singleton
    @provider
    def provideLogger(self) -> Logger:
        loggerLevel = 'DEBUG'
        try:
            loggerLevel = str.upper(os.environ['coral.apigateway.logging'])
            hasLoggerLevel = getattr(logging, loggerLevel, 'None') > 0
            if hasLoggerLevel:
                if loggerLevel not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                    loggerLevel = 'NOTSET'
        except:
            loggerLevel = 'NOTSET'

        logger = logging.getLogger('coralLogger')
        logger.setLevel(loggerLevel)
        if loggerLevel != 'NOTSET':
            ch = logging.StreamHandler()
            ch.setLevel(loggerLevel)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.propagate = False  # Do not propagate the message to be logged by the parents
            logger.addHandler(ch)
        else:
            logger.disabled = True
        return logger


instance = Injector([AppDi])
