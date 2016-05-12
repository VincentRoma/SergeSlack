#!/usr/bin/env python
# -*- coding: utf-8 -*-

import database_connector as DB
import requests
import params
import json

def get_all_user_info():
    payload = {'token': params.TOKEN}
    r = requests.post('https://slack.com/api/users.list', data=payload)
    response = json.loads(r.text)
    return response

def load_users():
    users = get_all_user_info()
    cursor, cnx = DB.open_connection()
    for user in users['members']:
        if not DB.user_already_exits(cursor, user) and not user['is_bot']:
            DB.insert_user(cursor, user)
    DB.close_connection(cursor, cnx)
    print "Serge has been initialized"

load_users()
