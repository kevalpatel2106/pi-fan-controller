# Raspberry Pi variable speed cooling fan controller
![Docker Build](https://github.com/kevalpatel2106/pi-fan-controller/workflows/build/badge.svg) ![GitHub release](https://img.shields.io/github/v/release/kevalpatel2106/pi-fan-controller)

Docker container that keeps the CPU temperature at desired level with DC fan (without PWM). If you have PWM enabled fan, please use [docker-rpi-fan](https://github.com/pilotak/docker-rpi-fan) instead.

## Docker-compose
```yaml
version: "3.7"
services:
  fan-controller:
    container_name: fan-controller
    restart: always
    image: ghcr.io/kevalpatel2106/pi-fan-controller:latest
    environment:
      - DESIRED_TEMP=45
      - FAN_PIN=12
    devices:
      - /dev/gpiomem
```

## Environmental variables
Bellow are all available variables

| Variable | Description | Default value |
| --- | --- | :---:|
| `DESIRED_TEMP` | Temperature it tries to keep it at | 50°C |
| `FAN_PIN` | GPIO Pin number where positive connected | 13 |
| `READ_INTERVAL` | How often read the temperature | 2 seconds |


