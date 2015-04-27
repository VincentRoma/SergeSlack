#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def message_formating(new_message):
    return json.dumps(new_message)


def new_message(text, chan):
    return message_formating({"id": 4, "type": "message", "channel": chan, "text": text})
