import re
import logging #todo

def extract_filter(query, key_character):
    pattern = '(?: |^)' + key_character + '(\w+|\"[\w ]+\")'
    match = re.search(pattern, query)
    filter = match and match.group(1)
    logging.debug(filter)
    if filter:
        sanitizedQuery = query.replace(key_character + filter, "")
        return sanitizedQuery, filter
    else:
        return query, None

def add_jql_filter(jql, filter_key, filter_value):
    if filter_value:
        return jql + ' and ' + filter_key + '=' + filter_value
    else:
        return jql

def get_results(jira, query):
    if jira.is_issue_key(query):
        jql = 'key="' + query + '" or text~"' + query + '*"'
    else:
        query, project = extract_filter(query, "@")
        query, issue_type = extract_filter(query, "#")
        textQuery = (query + '*') if not query[-1].isspace() else query.strip()
        jql = 'text~"' + textQuery + '"'
        jql = add_jql_filter(jql, "project", project)
        jql = add_jql_filter(jql, "issuetype", issue_type)
    return jira.get('/rest/api/3/search', {'jql': jql + ' order by lastViewed desc', 'fields': 'summary,issuetype'})

def add_item(wf, jira, issue):
    issue_key=issue['key']
    issue_url=jira.issue_url(issue_key)
    wf.add_item(
        title=issue['fields']['summary'],
        subtitle=issue['key'] + ' - ' + issue['fields']['issuetype']['name'],
        autocomplete=issue_key,
        arg=issue_url,
        valid=1
    )

search_issue_spec={
    'get_results': get_results,
    'extract_results': lambda json: json['issues'],
    'add_item': add_item 
}
