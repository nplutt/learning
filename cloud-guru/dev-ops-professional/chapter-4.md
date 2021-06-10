# Monitoring and Logging

## Cloudwatch Overview

#### What is Cloudwatch?
* Monitor your resources in AWS
  - A metric gathering service
  - A monitoring/alerting service
  - A graphing service
  - A logging service
  
#### Retention Period
* Data points < 60 seconds are available for 3 hours (high resolution)
* Data points ~= 60 seconds (1 minute) are available for 15 days
* Data points ~= 300 seconds (5 minutes) are available for 63 days
* Data points ~= 3600 seconds (1 hour) are available for 445 days (15 months)

If a data point starts out at 60 seconds it will be retained with that granularity for 15 days after which it will be moved to 300 seconds and so forth.

## CloudWatch Custom Metrics

