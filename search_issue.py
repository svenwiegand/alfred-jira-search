from jira import Jira
from util import add_no_result_item

def search_issue(wf, jira, query):
    def add_items_for_issues(issues):
        for issue in issues:
            issue_key=issue['key']
            issue_url=jira.issue_url(issue_key)
            wf.add_item(
                title=issue['key'],
                subtitle=issue['fields']['summary'],
                autocomplete=issue_key,
                arg=issue_url,
                valid=1
            )

    if jira.is_issue_key(query):
        jql = 'key=' + query + ' or text~"' + query + '"'
    else:
        jql = 'text~"' + query + '"'

    response = jira.get('/rest/api/3/search', {'jql': jql + ' order by lastViewed desc'})
    json = response.json()
    if 'total' in json and json['total'] > 0:
        add_items_for_issues(json['issues'])
    else:
        add_no_result_item(wf)