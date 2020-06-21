# Version 1.3,  2020-05-12
from tis.oneM2M import *
from comm.zb_lib import *
from socket import *


# Socket interface
host = '210.107.214.172'
port = 3105
sc = socket(AF_INET, SOCK_STREAM)
sc.connect((host, port))


# ZigBee interface
rf_sc = Xbee('COM6')


# TIS interface
tis_thread = TIS(Thing(), sc, rf_sc)
tis_thread.run()