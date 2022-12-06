from pydantic import BaseModel
from typing import List
import requests
import re


class participant(BaseModel):  # имя человека или название фирмы
    type: str = ''
    name: str = ''


class state(BaseModel):  # состояние дела
    Date: str = ''
    State: str = ''
    Document: str = ''


class document(BaseModel):  # состояние дела
    Date: str = ''
    Type: str = ''
    Url: str = None


class case(BaseModel):  # судебное дело запрошенное по имени
    Number: str = ''
    Url: str = ''
    State: str = ''
    StateDate: str = ''
    Judge: str = ''
    Codex: str = ''
    Category: str = ''
    participants: List[participant]


class case_from_url(BaseModel):  # судебное дело запрошенное по url
    CaseNumber: str = ''
    AppealRegisterDate: str = ''
    RegisterDate: str = ''
    EndDate: str = ''
    DecisionStartDate: str = ''
    Judge: str = ''
    Category: str = ''
    PreviousCaseNumber: str = ''
    State: str = ''
    Person: str = ''
    participants: List[participant]
    history: List[state]
    documents: List[document]


def court_case(name):
    """
    То же, что и court_cases(), только ищет по одному имени(либо краткому, либо полному)
    Принимает, возвращает аналогично.
    """
    url = f"https://service.api-assist.com/parser/mosgorsud_api/?key=dd48a3880956f92e995edeb40e131d13&participant={name}"
    response = requests.request("GET", url)
    all_court_cases = response.json()
    names_plaintiff = ['Мир Финансов', 'МИР Финансов', 'мир финансов', 'Мир финансов']
    name_type = ['УК', 'Управляющая Компания', 'Управляющая компания', 'ук']
    lst = []
    if int(all_court_cases['total_count']) > 0:
        lst = [case(**x) for x in all_court_cases['cases'] if any(
            s1 in x['participants'][0]['name'] and s2 in x['participants'][0]['name'] for s1 in names_plaintiff for s2
            in names_plaintiff)]
    return lst


def court_cases(name):
    '''
    Принимает строку: либо полное имя ответчика(Курдина Татьяна Александровна), либо краткоaе (Курдина Т.А.)
    Возвращает список дел по данному ответчику, где истец это "УК Мир финансов" и его производные.
    '''
    list_cases = []
    [list_cases.append(x) for x in court_case(name)]
    if '.' not in name:
        name = f"{name.split()[0]} {re.findall('[А-Я]', name)[1]}.{re.findall('[А-Я]', name)[2]}."
        [list_cases.append(x) for x in court_case(name)]
    return list_cases


def court_case_from_url(case):
    url = f"https://service.api-assist.com/parser/mosgorsud_api/?key=dd48a3880956f92e995edeb40e131d13&caseURL={case.Url}"
    response = requests.request("GET", url)
    return response.json()['case']


def court_cases_from_url(list_cases):
    list_cases_from_url = []
    [list_cases_from_url.append(case_from_url(**(court_case_from_url(x)))) for x in list_cases]
    return list_cases_from_url
