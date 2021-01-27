# Copyright 2021 Mark Winter (wintermarkedward@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time

from prometheus_client import start_http_server, Gauge

from grove.grove_PM2_5_HM3301 import Seeed_HM3301 as GroveDustSensor
from grove.grove_air_quality_sensor_v1_3 import GroveAirQualitySensor
from grove.grove_temperature_humidity_aht20 import GroveTemperatureHumidityAHT20
from grove.seeed_si114x import grove_si114x as GroveSunlightSensor


def run_server():
    dust_sensor = GroveDustSensor()
    air_sensor = GroveAirQualitySensor(0)
    temp_humid_sensor = GroveTemperatureHumidityAHT20()
    sunlight_sensor = GroveSunlightSensor()

    dust_pm1_gauge = Gauge('grovemonitoring_dust_pm1_0', 'Atmospheric PM1.0')
    dust_pm25_gauge = Gauge('grovemonitoring_dust_pm2_5', 'Atmospheric PM2.5')
    dust_pm10_gauge = Gauge('grovemonitoring_dust_pm10_0', 'Atmospheric PM10.0')

    air_gauge = Gauge('grovemonitoring_air_quality', 'Air Quality')

    temp_gauge = Gauge('grovemonitoring_temperature', 'Temperature Celcius')
    humid_gauge = Gauge('grovemonitoring_humidity', 'Humidity')

    visible_gauge = Gauge('grovemonitoring_visible_light', 'Visible Light')
    uv_gauge = Gauge('grovemonitoring_uv_light', 'UV Light')
    ir_gauge = Gauge('grovemonitoring_ir_light', 'IR Light')

    while True:
        pm1, pm2, pm10 = dust_sensor.read()
        dust_pm1_gauge.set(pm1)
        dust_pm25_gauge.set(pm2)
        dust_pm10_gauge.set(pm10)
        # print(f"PM1: {pm1}  PM2.5: {pm2}  PM10: {pm10}")

        air_quality = air_sensor.read()
        air_gauge.set(air_quality)
        # print(f"Air Quality: {air_quality}")

        temp, humid = temp_humid_sensor.read()
        temp_gauge.set(temp)
        humid_gauge.set(humid)
        # print(f"Temperature: {temp:.1f}C  Humidity: {humid:.1f}%")

        visible, uv, ir = sunlight_sensor.read()
        visible_gauge.set(visible)
        uv_gauge.set(uv)
        ir_gauge.set(ir)
        # print(f"Visible: {visible}  UV: {uv}  IR: {ir}")

        time.sleep(5)


if __name__ == "__main__":
    start_http_server(8000)
    run_server()

