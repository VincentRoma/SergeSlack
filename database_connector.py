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


def select_all_citation(cursor):

    query = ("SELECT * FROM Citation;")
    cursor.execute(query)

    return cursor


def insert_citation(cursor, citation, author):

    query = (u'INSERT INTO Citation (Citation, Author) VALUES ("{}", "{}")'.format(citation, author))
    print "Query: {}".format(query)
    cursor.execute(query)

    return cursor


def close_connection(cursor, cnx):

    cnx.commit()
    cursor.close()
    cnx.close()
