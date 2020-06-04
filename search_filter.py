def add_item(wf, jira, filter):
    wf.add_item(
        title=filter['name'],
        autocomplete=filter['name'],
        arg=jira.filter_url(filter['id']),
        valid=1
    )

search_filter_spec={
    'get_results': lambda jira, query: jira.get('/rest/api/3/filter/search', {'filterName': query}),
    'extract_results': lambda json: json['values'],
    'add_item': add_item 
}