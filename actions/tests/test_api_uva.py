import pytest
import os
import sys
import inspect
import api_uva
import requests
import json
from bs4 import BeautifulSoup
from rasa_core_sdk import Tracker
from actions.actions import UserForm
from actions.actions import CodeForm
from actions.actions import ActionFeedbackSubmissao

@pytest.fixture
def custom_domain():
    return {}

@pytest.fixture
def custom_tracker():
    return Tracker('', {}, {}, '', '', '', {}, '')

@pytest.fixture
def custom_tracker_feedback():
    return Tracker('', {'username':'usuario_teste'}, {}, '', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
    class Dispatcher():
        def utter_message(self, text=''):
            pass
    return Dispatcher()

@pytest.fixture
def custom_user_form():
    return UserForm();


def test_name_user_form(custom_user_form):
    name = custom_user_form.name();
    assert name == "user_form"

def test_required_slots_user_form(custom_user_form):
    slots = custom_user_form.required_slots(custom_tracker)
    assert slots == ['username', 'password']

def test_submit_user_form(custom_user_form, custom_dispatcher,
                          custom_tracker, custom_domain):
    slots = custom_user_form.submit(custom_dispatcher, 
                                custom_tracker, custom_domain)
    assert slots == [{"event": "slot", "timestamp": None,
                     "name": "username", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "password", "value": None}]


@pytest.fixture
def custom_code_form():
    return CodeForm();


def test_name_code_form(custom_code_form):
    name = custom_code_form.name()
    assert name == "code_form"

def test_required_slots_code_form(custom_code_form):
    slots = custom_code_form.required_slots(custom_tracker)
    assert slots == ['problema', 'linguagem', 'codigo']

def test_map_linguagem(custom_code_form):
    assert custom_code_form.map_linguagem('C') == '1'
    assert custom_code_form.map_linguagem('Java') == '2'
    assert custom_code_form.map_linguagem('C++') == '3'
    assert custom_code_form.map_linguagem('Pascal') == '4'
    assert custom_code_form.map_linguagem('C++ 11') == '5'
    assert custom_code_form.map_linguagem('Python 3') == '6'
    assert custom_code_form.map_linguagem('Sublime') == 'erro'

def test_submit_code_form(custom_code_form, custom_dispatcher,
                          custom_tracker, custom_domain):
    slots = custom_code_form.submit(custom_dispatcher, 
                                    custom_tracker, custom_domain)
    assert slots == []


@pytest.fixture
def custom_feedback_submissao():
    return ActionFeedbackSubmissao()


def test_name_feedback_submissao(custom_feedback_submissao):
    name = custom_feedback_submissao.name()
    assert name == "action_feedback_submissao_uva"

def test_run_feedback_submissao(custom_feedback_submissao, custom_dispatcher,
                                custom_tracker_feedback, custom_domain):
    username = custom_feedback_submissao.run(custom_dispatcher,
                                             custom_tracker_feedback,
                                             custom_domain)
    assert username == 'usuario_teste'


@pytest.fixture
def custom_session():
    session = requests.session()
    return session

@pytest.fixture
def custom_url():
    url = 'http://uva.onlinejudge.org/'
    return url


def test_get_params():
    texto = "<body></body>"
    form = BeautifulSoup(texto, features="html.parser")
    parametros = api_uva.get_params(form)
    assert parametros == {}

def test_get_soup(custom_session, custom_url):
    soup = api_uva.get_soup(custom_url)
    request = custom_session.get(custom_url)
    html = request.text
    custom_soup = BeautifulSoup(html, features="html.parser")
    assert soup.title == custom_soup.title

def test_make_login(custom_url):
    username = 'username'
    password = 'password'
    url_falso = 'https://www.google.com/'
    resultado = api_uva.make_login(username, password, url_falso)
    assert resultado == False
    username = 'username'
    password = 'password'
    resultado = api_uva.make_login(username, password, custom_url)
    assert resultado == False
    username = 'usuario_teste'
    password = '123456789'
    resultado = api_uva.make_login(username, password, custom_url)
    assert resultado == True

def test_get_code():
    path = 'actions/tests/teste.txt'
    resultado = api_uva.get_code(path)
    assert resultado == "testepytest"


@pytest.fixture
def custom_data_by_id():
    url = 'http://uhunt.felix-halim.net/api/p/id/2454'
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data

@pytest.fixture
def custom_data_by_number():
    url = 'http://uhunt.felix-halim.net/api/p/num/11459'
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data


def test_get_problem(custom_data_by_id, custom_data_by_number):
    resultado = api_uva.get_problem(None, None, True, True)
    assert resultado == None
    resultado = api_uva.get_problem('2454', None, True, False)
    assert resultado == custom_data_by_id
    resultado = api_uva.get_problem(None, '11459', False, True)
    assert resultado == custom_data_by_number
    resultado = api_uva.get_problem(None, None, False, False)
    assert resultado == None

def test_get_problem_by_id(custom_data_by_id):
    resultado = api_uva.get_problem_by_id('2454')
    assert resultado == custom_data_by_id 

def test_get_problem_by_number(custom_data_by_number):
    resultado = api_uva.get_problem_by_number('11459')
    assert resultado == custom_data_by_number

def test_submeter_um_problema():
    resultado = api_uva.submeter_um_problema('username', 'password',
                                             '11459', '5', '', 'codigo')
    assert resultado == 'UVa Online Judge'
    resultado = api_uva.submeter_um_problema('username', 'password',
                                             '11459', '5', 'actions/tests/teste.txt',
                                             'codigo')
    assert resultado == 'UVa Online Judge'

def test_username_para_userid():
   assert api_uva.username_para_userid('usuario_teste') == '1057837'

def test_resultado_ultima_submissao():
    assert api_uva.resultado_ultima_submissao('andreabenf') == 'Olha, o código rodou, mas sua solução não apresenta o resultado esperado para todos os casos de testes dos juízes, arrume e tente de novo!'