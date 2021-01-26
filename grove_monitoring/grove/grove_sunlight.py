import seeed_si114x


class GroveSunlightSensor:
    def __init__(self):
        self.sensor = seeed_si114x.grove_si114x()

    def read(self):
        visible = self.sensor.ReadVisible
        uv = self.sensor.ReadUV/100
        ir = self.sensor.ReadIR

        return visible, uv, ir
