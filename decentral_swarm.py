import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from cflib.crazyflie.log import LogConfig

uri_root = 'radio://0/80/2M/E7E7E7E7'
swarm = ['E5', 'E6', 'E7', 'E8', 'E9', 'EA']





if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    for id in swarm:
        uri = uri_root + id

        with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
