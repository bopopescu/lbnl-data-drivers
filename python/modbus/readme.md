# Modbus Python Driver

        ('string', decoder.decode_string(8)),
        ('bits', decoder.decode_bits()),
        ('8int', decoder.decode_8bit_int()),
        ('8uint', decoder.decode_8bit_uint()),
        ('16int', decoder.decode_16bit_int()),
        ('16uint', decoder.decode_16bit_uint()),
        ('32int', decoder.decode_32bit_int()),
        ('32uint', decoder.decode_32bit_uint()),
        ('32float', decoder.decode_32bit_float()),
        ('32float2', decoder.decode_32bit_float()),
        ('64int', decoder.decode_64bit_int()),
        ('64uint', decoder.decode_64bit_uint()),
        ('ignore', decoder.skip_bytes(8)),
        ('64float', decoder.decode_64bit_float()),
        ('64float2', decoder.decode_64bit_float())
