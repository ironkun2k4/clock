"""
Package wide configurations
"""
import os
import sys
from typing import Optional
from pathlib import Path
from threading import Lock
from dotenv import dotenv_values, find_dotenv, set_key


class ThreadSafeMeta(type):
    """
    A thread-safe implementation of Singleton
    """
    _instances: dict = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
          the returned instance
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    Global program configuration, uses the dotenv package to load runtime
      configuration from a .env file, once and only once into this object,
      this object can be used through-out the code base
    """
    try:
        __package = 'zoom_report'
        __version = '0.1.0'
        __default_env = 'dev'
        __logfile_name = f'{__package}-{__version}.log'
        __config = dotenv_values(find_dotenv())
        __env = __config['APP_ENV']
        __ragic_api_key = __config['RAGIC_API_KEY']
        __config_dir = (Path().home() / 'AppData' / 'Local' / __package
                        if os.name == 'nt'
                        else Path().home() / '.config' / __package)
        __ragic_opportunity_route = 'lynvolunteer/lyn-temp/5'
    except KeyError as error:
        sys.stderr.write(f"Dotenv config error: {error} is missing\n")
        sys.exit(1)

    @classmethod
    def package(cls) -> str:
        """
        Getter for package name
        """
        return cls.__package

    @classmethod
    def version(cls) -> str:
        """
        Getter for version of package
        """
        return cls.__version

    @classmethod
    def default_env(cls) -> str:
        """
        Getter for default env
        """
        return cls.__default_env

    @classmethod
    def logfile_name(cls) -> str:
        """
        Getter for logging file name
        """
        return cls.__logfile_name

    @classmethod
    def env(cls) -> Optional[str]:
        """
        Getter for config
        """
        return cls.__env

    @classmethod
    def ragic_api_key(cls) -> Optional[str]:
        """
        Getter for Ragic API key
        """
        return cls.__ragic_api_key

    @classmethod
    def config_dir(cls) -> Path:
        """
        Getter for config directory
        """
        return cls.__config_dir

    @classmethod
    def ragic_opportunity_route(cls) -> Path:
        """
        Getter for ragic opportunity route
        """
        return cls.__ragic_opportunity_route
