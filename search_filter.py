from jira import Jira
from util import add_no_result_item

def search_filter(wf, jira, query):
    def add_items_for_filters(filters):
        for filter in filters:
            wf.add_item(
                title=filter['name'],
                autocomplete=filter['name'],
                arg=jira.filter_url(filter['id']),
                valid=1
            )

    response = jira.get('/rest/api/3/filter/search', {'filterName': query})
    json = response.json()
    if 'total' in json and json['total'] > 0:
        add_items_for_filters(json['values'])
    else:
        add_no_result_item(wf)