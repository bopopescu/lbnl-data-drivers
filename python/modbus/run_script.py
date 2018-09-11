from modbus_driver import Modbus_Driver
import time
from struct import *

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder




obj = Modbus_Driver("config.yaml")


obj.initialize_modbus()
'''
signal_strength = obj.decode_register(200,'32int')
print(signal_strength)
print(type(signal_strength))
'''
'''
'''
#obj.write_coil(0,False)
'''
count = 0
while (count < 80):
    #print(count)
    print(str(count) + " is " + str(obj.read_coil(count)))
    print(str(count) + " is " + str(obj.read_discrete(count)))
    count = count + 1
'''
count = 0
while (count < 80):
    #print(count)
    print(str(count) + " is " + str(obj.read_coil(count)))
    print(str(count) + " is " + str(obj.read_discrete(count)))
    count = count + 1

#output = obj.get_data()
#print(output)
#obj.read_input(5)

f_value = obj.decode_register(100,'32float')
test = obj.decode_register(104,'32int')
signal_strength = obj.decode_register(106,'16int')
print("HOLDING FLOAT")
print(f_value)
print("HOLDING INT32")
print(test)
print("HOLDING INT16")
print(signal_strength)
print("INPUT FLOAT")
print(obj.decode_input_register(100,'32float'))
print("INPUT INT16")
print(obj.decode_input_register(106,'16int'))
obj.kill_modbus()
