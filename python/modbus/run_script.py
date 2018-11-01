from modbus_driver import Modbus_Driver
import time
from struct import *

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
#TODO make more comprehensive test script for Modbus_Driver()



obj = Modbus_Driver("config.yaml")


obj.initialize_modbus()

output = obj.get_data()
print(output)
out_list = obj.get_data_all_devices()
print("\ntest of get_data_all_devices\n")
print(out_list)

print("\ntest of get_data() with specific unit id\n")
output = obj.get_data(0x1)
print(output)

obj.kill_modbus()
