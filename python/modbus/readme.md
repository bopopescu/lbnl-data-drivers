

# Modbus Driver

[Here](https://github.com/cweyandt/lbnl-data-drivers/blob/master/python/modbus/run_script.py) is an example of how to create a Modbus_Driver object. An example config
file is [here](https://github.com/cweyandt/lbnl-data-drivers/blob/master/python/modbus/config.yaml)

### initialize_modbus(self):
Creates the connection with the modbus device using the method specified in the
config file.

### kill_modbus(self):
Closes the connection with the modbus device.

## Write functions

### write_data(self,register,value):

This function writes one value to one holding register. This value should be in
the form of a short int. For multiple register variables such as 32 bit floats
and 32 bit integers the value must be converted into a short int using pack
and unpack.

### write_coil(self,register,value):

This function writes one value that is True or False to the register specified.

## Read functions

### read_coil(self,register):

Reads coil register at address specified in the register argument.

### read_discrete(self,register):

Reads discrete register at address specified in the register argument.

### read_register_raw(self,register,length):

Reads holding register at address specified in the register argument and
continues to the (register + length). The object returned needs to decoded into
the appropriate type.

### read_input_raw(self,register,length):

Reads holding register at address specified in the register argument and
continues to the (register + length). The object returned needs to decoded into
the appropriate type.

### decode_register(self,register,type):

Reads holding register at address specified in the register argument. Multiple
registers may be read depending on the type specified.  The value is returned
as the type specified and does not need to be decoded. The types that can be
specified is listed below.


|   Type          | Length (registers) |
| ------------- |:------------------:|
|        ignore |                  1 |
|          8int |                  1 |
|         8uint |                  1 |
|         16int |                  1 |
|        16uint |                  1 |
|         32int |                  2 |
|        32uint |                  2 |
|       32float |                  2 |
|         64int |                  4 |
|        64uint |                  4 |
|       64float |                  4 |

### decode_input_register(self,register,type):

Reads input register at address specified in the register argument. Multiple
registers may be read depending on the type specified.  The value is returned
as the type specified and does not need to be decoded. The types that can be
specified is listed below.

### get_data(self):

Reads all the registers specified in the config file and returns them as a
dictionary. All register names in the config file must be unique. There is an
example of how the registers can be specified can be seen here.
