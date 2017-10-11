import httplib
import json
import time
import subprocess

#-----if want modify some varibles.modify below-----#
KNET_HTTP_ADDR = "127.0.0.1:8080"
KNET_HTTP_URL = "/knet/status"
KNET_TIME_OUT = 300
RESTART_SCRIPT_PATH = "/home/go/scripts/Python/knet/restart_knet.sh"
#-----if want modify some varibles.modify below-----#

def knet_restart():
	command = ['/bin/bash', '-x', RESTART_SCRIPT_PATH]
	return 0 == subprocess.call(command)

def knet_do(data):
	if data != "":
		j = json.loads(data) 
		if time.time() - j["knet"] > KNET_TIME_OUT:
			return knet_restart()
		if time.time() - j["sp"] > KNET_TIME_OUT:
			return knet_restart()
	else:
		return knet_restart()


	return False

def send_request():
	conn = httplib.HTTPConnection(KNET_HTTP_ADDR)
	try:
		conn.request("GET",KNET_HTTP_URL)
	except Exception as e:
		print e
		return ""
	resp = conn.getresponse()
	data = resp.read()
	conn.close()

	return data

def main():
	if knet_do(send_request()):
		print "process restart!"

if __name__ == "__main__":
	main()
