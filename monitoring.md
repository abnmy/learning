# Monitoring

## Tutos

* FCC OpenTelemetry Course - https://www.youtube.com/watch?v=r8UvWSX3KA8
* FCC Jenkins Tutorial - https://www.youtube.com/watch?v=f4idgaq2VqA
* FCC PagerDuty Clone - https://www.youtube.com/watch?v=4xuBT3BbsYU

## Tools

* uptime-kuma - [github repo](https://github.com/louislam/uptime-kuma) - self-hosted monitoring tool

## Grafana / Loki

### Relative time ranges: from date to date

#### today morning

from `now/d+2h` to `now/d-17h`, show today between 02:00 and 07:00

#### yesterday evening

from `now-1d/d+20h` to `now-1d/d-1h`: show yesterday between 20:00 to 23:00

#### past week

from `now - 1w/w` to `now - 1w/w`

## macOS

monitor_temp.sh

```sh
#!/bin/bash
while true; do
  sudo powermetrics --samplers smc | grep -i "CPU die temperature" >> ~/cpu_temps.log
  sleep 60
done
```

```sh
chmod +x monitor_temp.sh
nohup ./monitor_temp.sh &
```