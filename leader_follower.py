import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from cflib.crazyflie.log import LogConfig

uri = 'radio://0/80/2M/E7E7E7E7E6'
swarm = ['E5', 'E6', 'E7', 'E8', 'E9', 'EA']


def streamFormation(dx, dy, dz):
    cflib.crtp.init_drivers()

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf

        if cf.param.get_value('relative_ctrl.formation_dx') != dx:
            cf.param.set_value('relative_ctrl.formation_dx', dx);
        
        if cf.param.get_value('relative_ctrl.formation_dy') != dy:
            cf.param.set_value('relative_ctrl.formation_dy', dy);

        if cf.param.get_value('relative_ctrl.formation_dz') != dz:
            cf.param.set_value('relative_ctrl.formation_dz', dz);




if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()


