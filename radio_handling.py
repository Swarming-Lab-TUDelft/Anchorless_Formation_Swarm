import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

logging.basicConfig(level=logging.ERROR)



root = 'radio://0/80/2M/E7E7E7E7'
swarm = ['E6', 'E7', 'E8', 'E9', 'EA']


def streamFormation(id, dx_set, dy_set, dz_set):
    cflib.crtp.init_drivers()

    uri = root + swarm[id]

    try:
        print()
        print(f"Connection to {swarm[id]}...")
        with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
            cf = scf.cf
            print(f"Connection with {swarm[id]} successful!")

            time.sleep(0.5)
            all_params_set = False
            while not all_params_set:
                dx_is = float(cf.param.get_value('relative_ctrl.form_dx'))
                dy_is = float(cf.param.get_value('relative_ctrl.form_dy'))
                dz_is = float(cf.param.get_value('relative_ctrl.form_dz'))
                formationSet_is = int(cf.param.get_value('loco.formationSet'))


                if abs(dz_set - dz_is) < 0.001 and abs(dy_set - dy_is) < 0.001 and abs(dx_set - dx_is) < 0.001 and formationSet_is == 1:
                    print(f'All parameters for {swarm[id]} set: {dx_is}, {dy_is}, {dz_is}')
                    all_params_set = True;
                    return True;
                

                cf.param.set_value('relative_ctrl.form_dx', dx_set);
                time.sleep(0.2)

                cf.param.set_value('relative_ctrl.form_dy', dy_set);
                time.sleep(0.2)

                cf.param.set_value('relative_ctrl.form_dz', dz_set);
                time.sleep(0.2)

                cf.param.set_value('loco.formationSet', 1);
    except:
        print('Connection not possible.')
        return False;
            


def startLeader():
    cflib.crtp.init_drivers()

    uri = root + 'E5';

    try:
        print()
        print(f'Connecting to leader {uri}..')
        with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
            cf = scf.cf
            print('Connected to leader.')
            time.sleep(0.5)

            formationSet_is = int(cf.param.get_value('loco.formationSet'))

            while formationSet_is == 0:
                cf.param.set_value('loco.formationSet', 1)
                formationSet_is = int(cf.param.get_value('loco.formationSet'))

            print('Leader drone activated!')
            return True;
    except:
        print('Connection to leader failed.')
        return False;