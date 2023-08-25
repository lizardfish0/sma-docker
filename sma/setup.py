#!/usr/bin/env python

import os
import sys
import logging

from resources.readsettings import ReadSettings

autoProcess = os.path.join(os.environ.get("SMA_PATH", "/usr/local/sma"), "config/autoProcess.ini")


def main():
    # Ensure a valid config file
    ReadSettings()

    if not os.path.isfile(autoProcess):
        logging.error("autoProcess.ini does not exist")
        sys.exit(1)


if __name__ == '__main__':
    main()