# fuzzy-lamp
Tho goal of this project is to create a set of containers which can read data from 
smart energy meter and from ppv panels.
The following containers are part of this project:
1. Influxdb
2. Reader for smart energy meter (Python code)
3. Reader for ppv panels (Python code)
4. Python flask server to read and write data to the database
5. Dash python app to create a website to show the results

A docker compose file is present so the system can eb easily build with the command:
docker compose build
it can then be started with:
docker compose up

readme files in the separate parts explain how to different parts are and 
how everything can be configured

For now the development is done under windows, but the end goal is to run it all on a raspberry pi


