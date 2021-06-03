import re
import sys
import os
from workflow import Workflow3
from jira import Jira
from search_board import search_board_spec
from search_filter import search_filter_spec
from search_issue import search_issue_spec, search_jql_spec
from search_project import search_project_spec

search_specs = {
    'board': search_board_spec,
    'filter': search_filter_spec,
    'issue': search_issue_spec,
    'jql': search_jql_spec,
    'project': search_project_spec,
}

def search(wf, spec, query):
    jira = Jira()
    response = spec['get_results'](jira, query)
    json = response.json() if response.status_code == 200 else None
    if json and 'total' in json and json['total'] > 0:
        results = spec['extract_results'](json)
        for result in results:
            spec['add_item'](wf, jira, result)
    elif response.status_code < 400:
        wf.add_item(title='No results', subtitle='Try something else...', valid=0)
    else:
        wf.add_item(title='An error occured', subtitle="Maybe your query isn't valid...", valid=0)

def main(wf):
    search_key = wf.args[0]
    query = wf.args[1]
    search_spec = search_specs[search_key]
    search(wf, search_spec, query)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))