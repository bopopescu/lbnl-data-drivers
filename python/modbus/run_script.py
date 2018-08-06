from modbus_driver import Modbus_Driver
import time

obj = Modbus_Driver("config.ini")
obj.initialize_modbus()
result= obj.read_single_register(0x0552)
result2 = obj.read_single_register(0x060A)
print("result = ", result.registers[0]/10.0)
print("result2 = ", result2.registers[0])
result2 = obj.read_single_register(0x060A)
obj.write_data(0x060A,1)
result2 = obj.read_single_register(0x060A)
print("result2 = ", result2.registers[0])
obj.kill_modbus()
