#!/usr/bin/python
#--------------------------------------
#
#--------------------------------------
import httplib, urllib
import sys
import socket
# import logging
from pushover_config import pushover_config
# logging.basicConfig(filename=MQTT_LOG, level=logging.DEBUG)

if len(sys.argv)==2:

  myuser = pushover_config["user"]
  mytoken = pushover_config["token"]
  myurl = pushover_config["url"]

  mymessage = sys.argv[1]
  myhostname = socket.gethostname()

  mytitle = myhostname + " > notification."
  mymessage = "<p>" + mymessage + "</p>"

  conn = httplib.HTTPSConnection(myurl)
  conn.request("POST", "/1/messages.json",
    urllib.urlencode({
      "token": mytoken,
      "user": myuser,
      "html": "1",
      "title": mytitle,
      "message": mymessage,
      "sound": "intermission"
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()