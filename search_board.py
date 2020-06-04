from jira import Jira
from util import add_no_result_item

def search_board(wf, jira, query):
    def add_items_for_boards(boards):
        for board in boards:
            wf.add_item(
                title=board['name'],
                subtitle=board.get('location').get('name', '') if board.get('location') else '',
                autocomplete=board['name'],
                arg=jira.board_url(board['id']),
                valid=1
            )

    response = jira.get('/rest/agile/1.0/board', {'name': query})
    json = response.json()
    if 'total' in json and json['total'] > 0:
        add_items_for_boards(json['values'])
    else:
        add_no_result_item(wf)