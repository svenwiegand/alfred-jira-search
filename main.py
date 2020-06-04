import re
import sys
import os
from workflow import Workflow3
from jira import Jira
from search_board import search_board
from search_filter import search_filter
from search_issue import search_issue
from search_project import search_project

searchers = {
    'board': search_board,
    'filter': search_filter,
    'issue': search_issue,
    'project': search_project
}

def main(wf):
    search = wf.args[0]
    query = wf.args[1]
    jira = Jira(wf)
    searcher = searchers[search]
    searcher(wf, jira, query)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))