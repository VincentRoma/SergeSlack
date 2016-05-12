#!/usr/bin/env python
# -*- coding: utf-8 -*-

from messaging import new_message
import database_connector as DB
from random import randint
import requests
import params
import json

USERS = []

def treat_message(message, ws):
    if 'type' in message:
        if message['type'] == 'message':
            if 'serge' in message['text'] or 'Serge' in message['text']:
                respond_hello(message, ws)

def say_hello(ws):
    load_users()
    ws.send(new_message("Serge is there BITCHES", "C0GM3G459"))

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

def get_all_user_info():
    payload = {'token': params.TOKEN}
    r = requests.post('https://slack.com/api/users.list', data=payload)
    response = json.loads(r.text)
    return response

def load_users():
    cursor, cnx = DB.open_connection()
    USERS = DB.get_all_users(cursor)
    DB.close_connection(cursor, cnx)
