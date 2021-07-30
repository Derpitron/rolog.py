import time
from datetime import datetime
import os
from socket import gethostname
from traceback import format_exc
import psutil

from dhooks import Webhook
from dotenv import load_dotenv
from pytz import timezone
from requests import get

load_dotenv()
debug = Webhook(os.getenv('DEBUG'))
localtz = datetime.now(timezone(os.getenv('TIMEZONE')))

def getProcessByName(targetName):
	for proc in psutil.process_iter():
		try:
			if targetName.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess:
			pass
			return False:

def updateRobloxStatus():
    roblox = getProcessByName("RobloxPlayerBeta.exe")
	for roblox == none:
    	roblox = getProcessByName("RobloxPlayerBeta")
		if reset == False:
    		reset = True

		
	reset = False
	args = roblox.

try:
	hook = Webhook(os.getenv('HOOK'))
	debug.send("Script started on " + gethostname() + " with process ID: `" + str(os.getpid()) + "` at " + os.getenv('TIMEZONE') + " - " + localtz.strftime('%H:%M:%S') + " with interval of `" + os.getenv('INTERVAL') + "` seconds")
	while True:
		
		time.sleep(int(os.getenv('INTERVAL')))
except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")