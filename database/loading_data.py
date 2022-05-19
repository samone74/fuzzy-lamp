import os.path

import pandas as pd
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import arrow



csv = r'X:\smart_meter\2022\1\2smartmeter.csv'
pcsv = pd.read_csv(csv)


# You can generate an API token from the "API Tokens Tab" in the UI
token = "-32UKQpHtq007fPvK9CRxFZV4k3KRGgqjnjZK7mQlndE3n-ASg8_sZE-dbUKyqC5rLLFYMwZ3pmFCU3peOtY3Q=="
org = "home"
bucket = "smartmeter"
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    for month in range(1,13):
        print(month)
        for day in range(1,days_in_month[month - 1] + 1):
            print(day)
            csv = r'X:\smart_meter\2021\\' + str(month) + '\\' + str(day) + 'smartmeter.csv'
            if not os.path.exists(csv):
                continue
            pcsv = pd.read_csv(csv)
            for i in range(len(pcsv.gas)):

                date = datetime.strptime(pcsv.date[i], '%Y-%m-%d %H:%M:%S.%f')
                res2 = arrow.get(date, 'Europe/Amsterdam')
                point = Point("mem") \
                    .tag("host", "host1") \
                    .field("Gas2", pcsv.gas[i]) \
                    .time(res2.to('utc').datetime, WritePrecision.MS)
                write_api.write(bucket, org, point)

    client.close()

