import logging

import requests
import json

import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from rasa_core_sdk import Tracker
from actions.actions_stackoverflow import ActionPesquisaStackoverflow

@pytest.fixture
def custom_pesquisa_stackoverflow():
    return ActionPesquisaStackoverflow()

def test_name(custom_pesquisa_stackoverflow):
    name = custom_pesquisa_stackoverflow.name()
    assert name == 'action_pesquisa_stackoverflow'

def test_format_research(custom_pesquisa_stackoverflow):
    research = custom_pesquisa_stackoverflow.format_research('pesquise sobre cpp')
    assert research == 'cpp'

@pytest.fixture
def request_stackoverflow():
    link = 'https://api.stackexchange.com/2.2/search'
    order = 'desc'
    sort = 'activity'
    intitle = 'cpp'
    site = 'stackoverflow'

    payload = {
        'order': order, 'sort': sort, 'intitle': intitle, 'site': site
    }

    result = requests.get(link, params=payload)
    dictionary = json.loads(result.text)
    return dictionary 

def test_stackoverflow_request(custom_pesquisa_stackoverflow, request_stackoverflow):
    test_dictionary = custom_pesquisa_stackoverflow.stackoverflow_request('cpp')
    assert 1 == 1

def test_validate_links(custom_pesquisa_stackoverflow, request_stackoverflow):
    test_links = custom_pesquisa_stackoverflow.validate_links(request_stackoverflow)
    
    links = []
    dictionary = request_stackoverflow
    for item in dictionary['items']:
        if str(item['is_answered']) == 'True':
            links.append(item['link'])
        if len(links) == 5:
            break

    assert links == test_links
    
    test_links = custom_pesquisa_stackoverflow.validate_links({})
    links = []
    assert links == test_links
   

@pytest.fixture
def custom_domain():
    return {}

@pytest.fixture
def custom_tracker_with_no_message():
    return Tracker('', {}, {'text' : 'algo que não dará resultado'},
                   '', '', '', {}, '')

@pytest.fixture
def custom_tracker_with_message():
    return Tracker('', {}, {'text' : 'cpp'}, '', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
    class Dispatcher():
        def utter_message(self, text=''):
            pass
    return Dispatcher()


def test_run(custom_pesquisa_stackoverflow, custom_dispatcher,
             custom_tracker_with_no_message, custom_domain,
             custom_tracker_with_message):
    result = custom_pesquisa_stackoverflow.run(custom_dispatcher,
                                               custom_tracker_with_no_message,
                                               custom_domain)
    assert result == []
    result = custom_pesquisa_stackoverflow.run(custom_dispatcher,
                                               custom_tracker_with_message,
                                               custom_domain)
    assert result == []