from modbus_driver import Modbus_Driver
import time
from struct import *

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder




obj = Modbus_Driver("config.yaml")


obj.initialize_modbus()
"""
target_address = 0x601
while (target_address < 1623):
    previous_value = obj.decode_register(target_address,'16int')
    print(previous_value)
    add_value = 1
    if (previous_value < 0):
        obj.write_data(target_address,0)
    else:
        obj.write_data(target_address,(previous_value + add_value))
    current_value = obj.decode_register(target_address,'16int')
    print("The previous value at address " +str(target_address) + " was: " +str(previous_value))
    print("The current value at address " +str(target_address) + " is: " +str(current_value))
    target_address += 1
"""
#obj.write_data(0x655,0)

output = obj.get_data()
print(output)



obj.kill_modbus()
