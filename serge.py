#!/usr/bin/env python
# -*- coding: utf-8 -*-

from messaging import new_message
import database_connector
from random import randint
import requests
from params import params
import json
from quizz import Quizz
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

        # Add a citation
        elif 'add_citation' in message['text']:
            add_citation(ws, message)

        # Tell a Citation
        elif 'citation' in message['text']:
            tell_citation(ws, message['channel'])

        elif 'casse toi' in message['text']:
            kthxby(message, ws)

    if ('salut' in message['text']
    or 'hello' in message['text']
    or 'yo' in message['text']
    or 'Salut' in message['text']
    or 'Hello' in message['text']
    or 'Bonjour' in message['text']
    or 'bonjour' in message['text']):
        respond_hello(message, ws)


def say_hello(ws):
    ws.send(new_message("Serge is there BITCHES", "C02LLV4HS"))
    ask_question(ws)

def respond_hello(message, ws):
    user = get_user_info(message['user'])
    ws.send(new_message("Salut " + user['user']['profile']['first_name'] + ' !', message['channel']))


def kthxby(message, ws):
    ws.send(new_message("Kthxby Enculé", message['channel']))
    ws.close


def tell_citation(ws, chan):
    cursor, cnx = database_connector.open_connection('root', '', '127.0.0.1', 'Serge')
    citations_cursor = database_connector.select_all_citation(cursor)
    citations = []
    for row in citations_cursor:
        citations.append(row)
    citation = citations[randint(1, len(citations) - 1)]
    ws.send(new_message(citation['Citation'] + ' - ' + citation['Author'], chan))
    database_connector.close_connection(cursor, cnx)


def add_citation(ws, message):
    if secure_insert(message):
        command, citation, author = message['text'].split(",")
        print "command: {}, citation: {}, author: {}".format(command, citation, author)
        cursor, cnx = database_connector.open_connection('root', '', '127.0.0.1', 'Serge')
        database_connector.insert_citation(cursor, citation, author)
        ws.send(new_message("Nouvelle Citation Insérée! (CMB)", message['channel']))
        database_connector.close_connection(cursor, cnx)
    else:
        ws.send(new_message("Bien essayé !", message['channel']))


def secure_insert(message):
    if ('Marseille' not in message['text']
    or 'marseille' not in message['text']
    or 'OM' not in message['text']
    or 'sardine' not in message['text']):
        return True

    return False

def get_user_info(user):
    payload = {'token': params.TOKEN, 'user': user }
    r = requests.post('https://slack.com/api/users.info', data=payload)
    response = json.loads(r.text)
    return response
    
def ask_question(ws):
    questions = Quizz.all_question()
    ws.send(new_message(questions[0]['q_text'], "C02LLV4HS"))