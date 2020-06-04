def add_item(wf, jira, board):
    wf.add_item(
        title=board['name'],
        subtitle=board.get('location').get('name', '') if board.get('location') else '',
        autocomplete=board['name'],
        arg=jira.board_url(board['id']),
        valid=1
    )

search_board_spec={
    'get_results': lambda jira, query: jira.get('/rest/agile/1.0/board', {'name': query}),
    'extract_results': lambda json: json['values'],
    'add_item': add_item 
}