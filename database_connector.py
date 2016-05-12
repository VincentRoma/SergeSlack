#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


# FIXME: Use parameter
def open_connection(user=None, password=None, host=None, database=None):

    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='Serge')

    cursor = cnx.cursor(dictionary=True)

    return cursor, cnx


def close_connection(cursor, cnx):

    cnx.commit()
    cursor.close()
    cnx.close()


def insert_user(cursor, user):
    query = (u'INSERT INTO User (user_id, first_name, last_name) VALUES ("{}", "{}", "{}")'.format(user['id'],user['profile']['first_name'], user['profile']['last_name']))
    cursor.execute(query)


def user_already_exits(cursor, user):
    query = (u'SELECT * FROM User WHERE user_id="{}"'.format(user['id']))
    cursor.execute(query)
    res = cursor.fetchall()
    return len(res)
