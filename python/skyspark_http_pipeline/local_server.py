from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import requests as req
import urllib.parse
import yaml# pip install pyyaml
from alc_class import alc_client
from datetime import datetime

# Host name and port number that server will operate under for Skyspark to discover
hostName = "localhost"
hostPort = 9000

# URI and headers for Elastic Search POST request.
REMOTE_URI_NERSC = 'https://fn.nersc.gov/t/get_timeseries/get_timeseries'
REMOTE_HEADERS_NERSC = {"Content-Type": "application/json; charset=utf8"}

# Read in authentication credentials from yaml configuration file
with open('authentication.yaml', 'r') as file_auth:
	authentication_yaml = yaml.load(file_auth)

# Declare ALC client from alc_class.py with credentials from yaml file
ALC_CLIENT = alc_client(username=authentication_yaml['ALC']['username'],password=authentication_yaml['ALC']['password'])

# Fake Json for testing purposes. Remove when rolling out.
FAKE_JSON = json.dumps({"metric": "data.meter:output power|data.host:pdu11-fpc|data.modbus_point:Real Power", "hits": 19531, "value": [["2018-10-01T03:37:48.000Z", 30.0], ["2018-10-04T03:38:18.000Z", 30.0]]})


class MyServer(BaseHTTPRequestHandler):

	def do_GET(self):
		'''Defines a GET request handler for server http requests
		Parameters
		----------
		self : object
		class object that contains incoming URI from Skyspark. 
		Can reference URI path and parse accordingly.

		Returns
		-------
		None
		Returns no data to outer function, instead writes to requesting socket.
		
		'''

		if self.path.endswith("elastic"):
			unquoted_path = urllib.parse.unquote_plus(self.path)
			print("This is the path: ",unquoted_path)
			items = unquoted_path.split('?') # Payload = 1	
			data = items[1]
			
			ret = req.post(REMOTE_URI_NERSC, headers=REMOTE_HEADERS_NERSC,auth=(authentication_yaml['ElasticSearch']['username'],authentication_yaml['ElasticSearch']['password']),data=data)
			payload = json.dumps(ret.text)
			
			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
		
			# TODO: Confirm sent data is in format Skyspark likes
			
			self.wfile.write(payload.encode('utf-8'))

		elif self.path.endswith("alc"):
			unquoted_path = urllib.parse.unquote_plus(self.path)
			items = unquoted_path.split('?') # Log = 1, start_date = 2, end = 3
			data = [items[1]] # Logs go in as a list
			start_date = datetime.strptime(items[2], '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %I:%M:%S %p')

			end_date = datetime.strptime(items[3], '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %I:%M:%S %p')

			ret = ALC_CLIENT.collect_data(trend_log_paths=data, start_time=start_date, final_time=end_date)
			payload = json.dumps(ret)
			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(payload.encode('utf-8'))

# Declare HTTP server request object with declared hostname and port number.
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:# Run server forever or until keyboard termination.
    myServer.serve_forever()
except KeyboardInterrupt:
	print("Keyboard interrupt. Server terminated")
	myServer.socket.close()
