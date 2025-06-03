import pytest
from web_client.turn_dict_to_obj import *

# temporary
# from client_package.web_client.turn_dict_to_obj import *


def test_make_dict_to_obj():
    data = {'area': 10, 'date_of_introduction': 1970, 'designer': 'Garrett AiResearch', 'process': 100,
            'processor': 'MP944 (20-bit, 6-chip)', 'transistor_count': 'NA'}
    cpu1 = make_dict_to_obj(data)
    for key in data.keys():
        assert data[key] == cpu1.get_dict()[key]


def test_make_dict_to_obj1():
    with pytest.raises(ValueError):
        data = {"bad": "data"}
        make_dict_to_obj(data)


def test_make_list_of_dict_to_obj():
    data = [{'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 10, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 100, 'date_of_introduction': 1870, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000}]
    list_of_obj = make_list_of_dict_to_obj(data)
    for i in range(len(list_of_obj)):
        for key in data[0].keys():
            assert data[i][key] == list_of_obj[i].get_dict()[key]


def test_make_list_of_dict_to_obj1():
    with pytest.raises(ValueError):
        data = [{'bad': "data1"},
                {'bad': "data2"},
                {'area': 100, 'date_of_introduction': 1870, 'designer': 'cool designer', 'process': 100,
                 'processor': 'cool chip name', 'transistor_count': 10000000}]
        make_list_of_dict_to_obj(data)
