## Grove Monitoring

Python Server that reads Grove Room Sensors and exports the values for Prometheus scraping

The sensors are read every 5 seconds


### Required Hardware

- Raspberry PI. Tested on Raspberry Pi 4 Model B

- [Grove Base Hat](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/)

- [Grove Sunlight Sensor](https://wiki.seeedstudio.com/Grove-Sunlight_Sensor/)

- [Grove AHT20 Temperature & Humidity Sensor](https://wiki.seeedstudio.com/Grove-AHT20-I2C-Industrial-Grade-Temperature&Humidity-Sensor/)

- [Grove Laser PM2.5 Dust Sensor](https://wiki.seeedstudio.com/Grove-Laser_PM2.5_Sensor-HM3301/)

- [Grove Air Quality Sensor v1.3](https://wiki.seeedstudio.com/Grove-Air_Quality_Sensor_v1.3/)


### Installation

- Edit the `User` field in `systemd/grovemonitoring.service` to your linux account

- Install the systemd service to /etc/systemd/system/grovemonitoring.service


```SHELL
$ sudo cp systemd/grovemonitoring.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl start grovemonitoring
$ sudo systemctl status grovemonitoring
$ sudo systemctl enable grovemonitoring  # Enable on boot
```

- Check the exported metrics at `localhost:8000`
