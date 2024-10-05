from pyrustools.client_plus import MyPyrus
from pyrustools.object_methods import object_by_code

def comment_task_before_consideration(task_number): # получает на вход номер дела, достает начальную информацию о нем с сайта и заполняет задчу в пайрусе
    elem_MyPyrus = MyPyrus(login="", security_key="")
    elem_MyPyrus.initialize()
    task_getter = elem_MyPyrus.get_task(task_number)
    elem_MyPyrus.update_task_field_info(task_getter.task)
    defendant_name = object_by_code(task_getter.task.flat_fields, 'u_defendant_fio').value
    cases = court_cases(defendant_name)
    url_cases = court_cases_from_url(cases)
    elem_MyPyrus.comment_task_plus(
            task_id=task_number,
            field_updates=initial_field_updates_form(cases, url_cases),
            text='Мониторинг судебных заседаний')
