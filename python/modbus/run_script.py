from modbus_driver import Modbus_Driver
import time
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

obj = Modbus_Driver("config.yaml")


obj.initialize_modbus()
signal_strength = obj.decode_register(199,'32int')
print(signal_strength)
output = obj.get_data()
print(output)

obj.kill_modbus()
