#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import websocket
import json
import serge
from params import params

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# https://slack.com/oauth/authorize
#
# https://slack.com/api/rtm.start


print bcolors.OKBLUE + 'Asking for WebSocket URL...' + bcolors.ENDC
session = requests.get("https://slack.com/api/rtm.start?token={}".format(params.TOKEN))
response = json.loads(session.text)

if response['ok']:
    print bcolors.OKGREEN + 'Url Acquired...' + bcolors.ENDC
    ws = websocket.create_connection(response['url'])

    print bcolors.OKGREEN + 'Connection Alive...' + bcolors.ENDC
    serge.say_hello(ws)

    while True:
        result = ws.recv()
        print bcolors.OKBLUE + "Treating Message..." + bcolors.ENDC
        print bcolors.WARNING + "{}".format(result) + bcolors.ENDC
        serge.treat_message(json.loads(result), ws)
    ws.close()

else:
    print bcolors.FAIL + 'Error while asking for websocket!'
    print 'Exit with code {} : {}'.format(response['code'], response['error']) + bcolors.ENDC
