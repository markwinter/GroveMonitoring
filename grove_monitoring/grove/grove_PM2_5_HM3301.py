
#
# Library for Grove - PM2.5 PM10 detect sensor (HM3301)
#

'''
## License

The MIT License (MIT)

Copyright (C) 2018  Seeed Technology Co.,Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''




from smbus2 import SMBus, i2c_msg
import time


HM3301_DEFAULT_I2C_ADDR = 0x40
SELECT_I2C_ADDR = 0x88
DATA_CNT = 29

class Seeed_HM3301(object):
    def __init__(self,bus_nr=1):
            
        self.PM_1_0_conctrt_std = 0         # PM1.0 Standard particulate matter concentration Unit:ug/m3
        self.PM_2_5_conctrt_std = 0         # PM2.5 Standard particulate matter concentration Unit:ug/m3
        self.PM_10_conctrt_std = 0          # PM10  Standard particulate matter concentration Unit:ug/m3
    
        self.PM_1_0_conctrt_atmosph = 0     #PM1.0 Atmospheric environment concentration ,unit:ug/m3
        self.PM_2_5_conctrt_atmosph = 0     #PM2.5 Atmospheric environment concentration ,unit:ug/m3
        self.PM_10_conctrt_atmosph = 0      #PM10  Atmospheric environment concentration ,unit:ug/m3


        with SMBus(bus_nr) as bus:
            write = i2c_msg.write(HM3301_DEFAULT_I2C_ADDR,[SELECT_I2C_ADDR])
            bus.i2c_rdwr(write)

    def read(self):
        data = self.read_data()

        pm1 = data[10]<<8 | data[11]          
        pm2 = data[12]<<8 | data[13]
        pm10 = data[14]<<8 | data[15]

        return pm1, pm2, pm10

    def read_data(self):        
        with SMBus(1) as bus:
            read = i2c_msg.read(HM3301_DEFAULT_I2C_ADDR,DATA_CNT)
            bus.i2c_rdwr(read)
            return list(read)

    def check_crc(self,data):
        sum = 0
        for i in range(DATA_CNT-1):
            sum += data[i]
        sum = sum & 0xff
        #print(sum)
        #print(data[28])
        return (sum==data[28])

