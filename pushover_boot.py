#!/usr/bin/python
#--------------------------------------
#
#--------------------------------------
import httplib, urllib
import sys
import socket
import subprocess

def get_ip(interface):
  ip_address=""
  try:
    process = subprocess.Popen(['ifconfig', interface],stdout=subprocess.PIPE,universal_newlines=True)
    ifconfig_output=process.communicate()[0]
    x=ifconfig_output.find("inet ")
    if x>0:
      y=ifconfig_output.find(" ",x+5)
      ip_address=ifconfig_output[x+5:y]
  except:
    pass
  return ip_address

if len(sys.argv)==4:

  myip = sys.argv[1]
  myuser = sys.argv[2]
  mytoken = sys.argv[3]

  myhostname = socket.gethostname()
  wlan0_address = get_ip("wlan0")

  mytitle = myhostname + " > booted."
  mymessage ="<p>" + myhostname + " > booted.</p>"

  if wlan0_address.strip():
    mymessage+="<p>IP (wlan0): <a href='http://"+wlan0_address+"'>"+wlan0_address+"</p>"

  mymessage+="<p>Internal IP: <a href='http://"+myip+"'>"+myip+"</a></p>"

  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.urlencode({
      "token": mytoken,
      "user": myuser,
      "html": "1",
      "title": mytitle,
      "message": mymessage,
      "sound": "cosmic"
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()