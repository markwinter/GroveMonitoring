#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.

from .adc import ADC

class GroveAirQualitySensor:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    def read(self):
        return self.adc.read(self.channel)
