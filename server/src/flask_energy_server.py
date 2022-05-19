from flask import Flask, request
from datetime import datetime
import arrow
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# write data to database

# get data from the database

app = Flask(__name__)


@app.route('/test')
def test():
    return {"test":2}

@app.route('/add_measurement', methods=['POST'])
def add_measurement():
    input_request = request.json
    bucket = input_request['type']
    date, ret_code = convert_date(input_request['date'])  # create datetime object for database
    if ret_code != 200:
        return date, ret_code
    value = input_request['value']
    # input checking
    if not isinstance(type, str):
        return 'Type is not a string', 401

    if isinstance(value, str):
        try:
            value = float(value)
        except ValueError:
            return 'Incorrect format for measurement', 401

    # writing to database
    # TODO get settings of database from config file
    # TODO based on type write to correct bucket
    # TODO check if bucket exists in database
    # TODO add logging
    token = "-32UKQpHtq007fPvK9CRxFZV4k3KRGgqjnjZK7mQlndE3n-ASg8_sZE-dbUKyqC5rLLFYMwZ3pmFCU3peOtY3Q=="
    org = "home"
    bucket = "smartmeter"
   # with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
   #     write_api = client.write_api(write_options=SYNCHRONOUS)
   #     point = Point("mem") \
   #         .tag("host", "host1") \
   #         .field("Gas2", value) \
   #         .time(date, WritePrecision.MS)
   #     write_api.write(bucket, org, point)
    return f'added measurement', 201


@app.route('/get_measurement', methods=['GET'])
def get_measurement():
    input_request = request.json
    bucket = input_request['type']
    start_date, ret_code = convert_date(input_request['start_date'])  # create datetime object for database
    if ret_code != 200:
        return start_date, ret_code
    end_date, ret_code = convert_date(input_request['end_date'])  # create datetime object for database
    if ret_code != 200:
        return end_date, ret_code


def convert_date(date: str):
    # converts the input data string to a utc datetime string for influxdb
    if not isinstance(date, str):
        return 'date is not a string', 401
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        return 'date not in correct format use: %Y-%m-%d %H:%M:%S.%f', 401
    date_arrow = arrow.get(date_obj, 'Europe/Amsterdam')
    return date_arrow.to('utc').datetime, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
