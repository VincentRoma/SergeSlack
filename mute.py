import requests
import json

r = requests.get('https://slack.com/api/channels.history?token=xoxp-16716527477-16720097713-40092022630-b78a6273c8&channel=C0GM3G459')
response = json.loads(r.text)
for message in response['messages']:

        if message['user'] == 'U15AR3F9C':
            r = requests.get('https://slack.com/api/chat.delete?token=xoxp-16716527477-16720097713-40092022630-b78a6273c8&ts={}&channel=C0GM3G459'.format(message['ts']))
            print "DELETED MESSAGE"
