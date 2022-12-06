def date(s):
  return f"{s[6:10]}-{s[3:5]}-{s[:2]}"

def initial_field_updates_form(case, url_case):

    field_updates = [{'id': 19,
                      'type': 'date',
                      'name': 'Дата поступления',
                      'tooltip': '',
                      'value': ''},
                    {'id': 18,
                      'type': 'text',
                      'name': 'Текущее состояние дела',
                      'tooltip': '',
                      'value': ''},
                    {'id': 20,
                      'type': 'table',
                      'name': 'История состояний',
                      'tooltip': '',
                      'value': []},
                    {'id': 8,
                      'type': 'text',
                      'name': 'Номер дела',
                      'tooltip': '',
                      'value': ''},
                    {'id': 9,
                      'type': 'text',
                      'name': 'Ссылка на номер дела в суде',
                      'tooltip': '',
                      'value': ''},
                    {'id': 10,
                      'type': 'text',
                      'name': 'Судья',
                      'tooltip': '',
                      'value': ''}]

    field_updates[0]['value'] = date(url_case[0].RegisterDate)
    field_updates[1]['value'] = case[0].State
    field_updates[3]['value'] = case[0].Number
    field_updates[4]['value'] = f"https://mos-gorsud.ru{case[0].Url}"
    field_updates[5]['value'] = case[0].Judge

    for i, x in enumerate(url_case[0].history):

        cells = [{'id': 21,
                  'type': 'date',
                  'name': 'Дата',
                  'tooltip': '',
                  'parent_id': 20,
                  'value': ''},
                {'id': 22,
                  'type': 'text',
                  'name': 'Состояние',
                  'tooltip': '',
                  'parent_id': 20,
                  'value': ''}]
                  
        cells[0]['value'] = date(x.Date)
        cells[1]['value'] = x.State
        field_updates[2]['value'].append({'row_id': i, 'cells': cells})
    return field_updates
