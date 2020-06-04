def add_item(wf, jira, project):
    wf.add_item(
        title=project['name'],
        subtitle=project['key'],
        autocomplete=project['name'],
        arg=jira.project_url(project['key']),
        valid=1
    )

search_project_spec={
    'get_results': lambda jira, query: jira.get('/rest/api/3/project/search', {'query': query}),
    'extract_results': lambda json: json['values'],
    'add_item': add_item 
}
