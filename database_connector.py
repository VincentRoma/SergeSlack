#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


# FIXME: Use parameter
def open_connection(user, password, host, database):

    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='Serge')

    cursor = cnx.cursor(dictionary=True)

    return cursor, cnx

def close_connection(cursor, cnx):

    cnx.commit()
    cursor.close()
    cnx.close()
