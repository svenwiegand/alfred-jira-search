import re

def extract_filter(query, key_character):
    pattern = '(?: |^)' + key_character + '(\w+|\"[\w ]+\")'
    match = re.search(pattern, query)
    filter = match and match.group(1)
    if filter:
        sanitizedQuery = query.replace(key_character + filter, "")
        return sanitizedQuery, filter
    else:
        return query, None

def query_terms(query):
    sanitized = re.sub('[-+!"]', ' ', query)
    return sanitized.split(' ')

def terms_jql(terms):
    def term_jql(term):
        return 'text~"' + term + '*"'
    nonEmptyTerms = filter(lambda term: len(term.strip()) > 0, terms)
    termSearches = map(term_jql, nonEmptyTerms)
    return " AND ".join(termSearches)

def add_jql_filter(jql, filter_key, filter_value):
    if filter_value:
        return jql + ' AND ' + filter_key + '=' + filter_value
    else:
        return jql

def get_issue_search_results(jira, query):
    if jira.is_issue_key(query):
        jql = 'key="' + query + '" or text~"' + query + '*"'
    else:
        query, project = extract_filter(query, "@")
        query, issue_type = extract_filter(query, "#")
        jql = terms_jql(query_terms(query))
        jql = add_jql_filter(jql, "project", project)
        jql = add_jql_filter(jql, "issuetype", issue_type)
    return get_jql_results(jira, jql)

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

def get_jql_results(jira, jql):
    return jira.get('/rest/api/3/search', {'jql': jql + ' order by lastViewed desc', 'fields': 'summary,issuetype'})

search_issue_spec={
    'get_results': get_issue_search_results,
    'extract_results': lambda json: json['issues'],
    'add_item': add_item 
}

search_jql_spec={
    'get_results': get_jql_results,
    'extract_results': lambda json: json['issues'],
    'add_item': add_item 
}