#!/usr/bin/env python
# -*- coding: utf-8 -*-

from messaging import new_message
import database_connector
from random import randint
import requests
from params import params
import json

def treat_message(message, ws):
    if 'type' in message:
        if message['type'] == 'message':
            answer(message, ws)

def say_hello(ws):
    ws.send(new_message("Serge is there BITCHES", "C0GM3G459P"))

def respond_hello(message, ws):
    user = get_user_info(message['user'])
    ws.send(new_message("Salut " + user['user']['profile']['first_name'] + ' !', message['channel']))

def kthxby(message, ws):
    ws.send(new_message("Kthxby Enculé", message['channel']))
    ws.close

def get_user_info(user):
    payload = {'token': params.TOKEN, 'user': user }
    r = requests.post('https://slack.com/api/users.info', data=payload)
    response = json.loads(r.text)
    return response
