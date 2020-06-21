# Version 1.3,  2020-05-13
from tis.oneM2M import *
from socket import *
from device.sensorhat import *


# Socket interface
host = '210.107.214.172'
port = 3105

# TIS for Sensor
sensor_sc = socket(AF_INET, SOCK_STREAM)
sensor_sc.connect((host, port))
sensor_tis = TIS(Sensor(), sensor_sc)
sensor_tis.start()

# TIS for Panel
panel_sc = socket(AF_INET, SOCK_STREAM)
panel_sc.connect((host, port))
panel_tis = TIS(Panel(), panel_sc)
panel_tis.start()