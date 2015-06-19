#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from params import params
import json

class Quizz:
    
    @staticmethod
    def all_question():
        r = requests.get("https://pareshchouhan-trivia-v1.p.mashape.com/v1/getRandomQuestion",
          headers={
            "X-Mashape-Key": "SeDWu0VRo1mshhv2V2VoFTPfQ1dGp1tk1Lyjsn5O6bvsurWBly",
            "Accept": "application/json"
          }
        )
        response = json.loads(r.text)
        return response