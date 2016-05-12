#!/usr/bin/env python
# -*- coding: utf-8 -*-

from messaging import new_message
import database_connector as DB
from random import randint
import requests
import params
import json

def treat_message(message, ws):
    if 'type' in message:
        if message['type'] == 'message':
            answer(message, ws)

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
    users = get_all_user_info()
    cursor, cnx = DB.open_connection()
    for user in users['members']:
        if not DB.user_already_exits(cursor, user):
            DB.insert_user(cursor, user)
    DB.close_connection(cursor, cnx)
