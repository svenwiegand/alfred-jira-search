from jira import Jira
from util import add_no_result_item

def search_project(wf, jira, query):
    def add_items_for_projects(projects):
        for project in projects:
            wf.add_item(
                title=project['name'],
                subtitle=project['key'],
                autocomplete=project['name'],
                arg=jira.project_url(project['key']),
                valid=1
            )

    response = jira.get('/rest/api/3/project/search', {'query': query})
    json = response.json()
    if 'total' in json and json['total'] > 0:
        add_items_for_projects(json['values'])
    else:
        add_no_result_item(wf)