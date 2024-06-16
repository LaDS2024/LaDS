import logging
from pathlib import Path

# APOLLO CONFIGURATION ==============================
PERCEPTION_FREQUENCY = 25
"""Rate at which the Message Broker publishes perception messages"""
APOLLO_VEHICLE_LENGTH = 4.933
"""Length of default Apollo vehicle"""
APOLLO_VEHICLE_WIDTH = 2.11
"""Width of default Apollo vehicle"""
APOLLO_VEHICLE_HEIGHT = 1.48
"""Height of default Apollo vehicle"""
APOLLO_VEHICLE_back_edge_to_center = 1.043
"""Length between the back edge and the center of default Apollo vehicle"""


# DIRECTORIES =======================================
APOLLO_ROOT = '/home/lily/study/Doppel/BaiduApollo_DoppelTest'
"""Root directory of Apollo 7.0"""
DT_ROOT = '/home/lily/study/Doppel/DoppelTest'
"""Root directory of DoppelTest"""
RECORDS_DIR = f'{DT_ROOT}/data/records'
"""Desired directory to save record files"""
LOG_DIR = f'{DT_ROOT}/data/Logs'
"""Desired directory to save log files"""

# DoppelTest CONFIGS ====================================
STREAM_LOGGING_LEVEL = logging.INFO
"""Global logging level"""
USE_SIM_CONTROL_STANDALONE = True
"""Whether you wish to use extracted SimControl when executing scenario"""
FORCE_INVALID_TRAFFIC_CONTROL = False
"""Whether you wish to force invalid traffic cnotrol (e.g., every signal being green)"""
SCENARIO_UPPER_LIMIT = 30
"""The length of each scenario (in seconds)"""
INSTANCE_MAX_WAIT_TIME = 10
"""The maximum time before the last ADS instance starts moving"""
# apollo num 3
MAX_ADC_COUNT = 3
"""Number of ADS instances you wish to run simultaneously"""
MAX_PD_COUNT = 0
"""Number of pedestrians you wish to include in simulations"""
RUN_FOR_HOUR = 12
"""Number of hours you wish to run"""
HD_MAP_PATH = f'{DT_ROOT}/data/maps/borregas_ave_fix/base_map.bin'
"""
The HD map you are currently using

:note: you also need to update ``apollo/modules/common/data/global_flagfile.txt``
  to match the HD map you are using
"""
