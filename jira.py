import base64
import os
import re
from workflow import Workflow3, web

issue_key_pattern = r'[a-zA-Z]+-[0-9]+'
domain = os.environ['domain']
username = os.environ['username']
password = os.environ['password']
default_params = {
    'fields': 'issuetype,project,summary',
    'max_results': 20
}

def full_params(params):
    p = default_params.copy()
    p.update(params)
    return p

class Jira:
    def __init__(self):
        self.base_url = 'https://' + domain
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic ' + base64.b64encode((username + ':' + password).encode('ascii'))
        }

    def url(self, path):
        return self.base_url + path

    def get(self, path, params = None):
        r = web.get(
            self.url(path), 
            params=full_params(params),
            headers=self.headers
        )
        return r

    def issue_url(self, key):
        return self.url('/browse/' + key)

    def board_url(self, id):
        return self.url('/secure/RapidBoard.jspa?rapidView=' + str(id))

    def filter_url(self, id):
        return self.url('/issues/?filter=' + str(id))

    def project_url(self, key):
        return self.url('/browse/' + key)

    def is_issue_key(self, str):
        return re.match(issue_key_pattern, str)
