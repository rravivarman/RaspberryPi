from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

celcius = sensor.get_object_1();
faren = (celcius*1.8)+32
print("Body Temperature : ",(round(celcius,2)))

ambient = sensor.get_ambient()
limited_ambient = round(ambient, 2)
print ("Ambient Temperature :", limited_ambient,u"\N{DEGREE SIGN}C")

bus.close()
