#!/usr/bin/env python
# -*- coding: utf-8 -*-

from messaging import new_message
import database_connector
from random import randint
# randint is inclusive


def treat_message(message, ws):
    if 'type' in message:
        if message['type'] == 'message':
            answer(message, ws)


def answer(message, ws):
    if '<@U04JBV6SR>' in message['text']:
        # Wake up thibs
        if '/CallThibs' in message['text']:
            ws.send(new_message("@Thibs: Suce des bites", message['channel']))

        # Tell a Citation
        if 'citation' in message['text']:
            tell_citation(ws, message['channel'])
    # if message['user'] == u'U02LNH2RW':
    #     ws.send(new_message("Ferme ta gueule Greg", message['channel']))


def say_hello(ws):
    ws.send(new_message("Serge is there BITCHES", "C04JVPWBP"))


def send_anwser(ws):
    pass


def tell_citation(ws, chan):
    cursor, cnx = database_connector.open_connection('root', '', '127.0.0.1', 'Serge')
    citations_cursor = database_connector.select_all_citation(cursor)
    citations = []
    for row in citations_cursor:
        citations.append(row)
    citation = citations[randint(1, len(citations) - 1)]
    ws.send(new_message(citation['Citation'] + ' - ' + citation['Author'], chan))
    database_connector.close_connection(cursor, cnx)
