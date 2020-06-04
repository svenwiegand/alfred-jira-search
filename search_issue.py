def get_results(jira, query):
    if jira.is_issue_key(query):
        jql = 'key="' + query + '" or text~"' + query + '*"'
    else:
        jql = 'text~"' + query + '*"'
    return jira.get('/rest/api/3/search', {'jql': jql + ' order by lastViewed desc'})

def add_item(wf, jira, issue):
    issue_key=issue['key']
    issue_url=jira.issue_url(issue_key)
    wf.add_item(
        title=issue['key'],
        subtitle=issue['fields']['summary'],
        autocomplete=issue_key,
        arg=issue_url,
        valid=1
    )

search_issue_spec={
    'get_results': get_results,
    'extract_results': lambda json: json['issues'],
    'add_item': add_item 
}
