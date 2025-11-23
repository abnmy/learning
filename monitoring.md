# Monitoring

## Tutos

* FCC OpenTelemetry Course - https://www.youtube.com/watch?v=r8UvWSX3KA8
* FCC Jenkins Tutorial - https://www.youtube.com/watch?v=f4idgaq2VqA
* FCC PagerDuty Clone - https://www.youtube.com/watch?v=4xuBT3BbsYU

## Tools

* Uptime Kuma: https://github.com/louislam/uptime-kuma - https://uptime.kuma.pet/
* SigNoz (alternative to DataDog): https://github.com/SigNoz/signoz - https://signoz.io/

## Grafana / Loki

### Relative time ranges from > to

Today morning: `now/d+2h` > `now/d-17h` = today:0h+2h > today:24h-17h = today between 2h > 7h

Yestarday evening: `now-1d/d+20h` > `now-1d/d-1h` = today-1d:0h+20h > today-1d:24h-1h = yesterday between 20h > 23h

Past week: `now - 1w/w` > `now - 1w/w`
