import pytest
from web_client.main import *
from web_client.turn_dict_to_obj import *

# temporary imports
# from client_package.web_client.main import *
# from client_package.web_client.turn_dict_to_obj import *




def test_home_message():
    expected_res = {'authors': ['William Ambrosetti', 'Youssef Sedra'], 'message': 'welcome to our web service',
                    'methods': ['get_component_names', 'get_components_features', 'get_all_collections',
                                'get_a_collection', 'check_if_component_exists', 'get_specific_component_s', 'add_data',
                                'add_many', 'update_a_component', 'delete_component_s', 'delete_collection',
                                'plot_components']}
    results = home_message()
    assert results == expected_res


def test_get_component_names():
    expected_res = ['gpu', 'cpu', 'ram']
    results = get_component_names()
    assert set(results) == set(expected_res)


def test_get_components_features():
    expected_res = ['area', 'date_of_introduction', 'designer', 'process', 'processor', 'transistor_count']
    results = get_components_features("cpu")
    assert expected_res == results


def test_get_components_features1():
    expected_res = {'cpu': ['area',
                            'date_of_introduction',
                            'designer',
                            'process',
                            'processor',
                            'transistor_count'],
                    'gpu': ['area',
                            'date_of_introduction',
                            'designer_s',
                            'manufacturer_s',
                            'process',
                            'processor',
                            'transistor_count'],
                    'ram': ['area',
                            'bit_units',
                            'capacity_bits',
                            'chip_name',
                            'date_of_introduction',
                            'manufacturer_s',
                            'process',
                            'ram_type',
                            'transistor_count']}
    results = get_components_features(None)
    assert expected_res == results


def test_get_components_features2():
    with pytest.raises(ValueError):
        bad_collection = "bad"
        get_components_features(bad_collection)


def test_get_all_collections():
    result = get_all_collections()
    expected_res = list
    assert isinstance(result, expected_res)
    assert result != []


def test_get_a_collection():
    result = get_a_collection("cpu")
    expected_res = list
    assert isinstance(result, expected_res)
    assert result != []


def test_get_a_collection1():
    with pytest.raises(ValueError):
        bad_collection = "bad"
        get_a_collection(bad_collection)


def test_check_if_component_exists():
    component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                      'processor': 'cool chip name', 'transistor_count': 10000000}
    delete_component_s("cpu", component_data)
    assert check_if_component_exists(component_data) == False


def test_check_if_component_exists1():
    component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                      'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", component_data)
    assert check_if_component_exists(component_data) == True


def test_check_if_component_exists2():
    invalid_data = {"invalid": "component_data"}
    result = check_if_component_exists(invalid_data)
    assert result == False


def test_get_specific_component_s():
    component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                      'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", component_data)
    result = get_specific_component_s("cpu", component_data)
    expected_res = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                    'processor': 'cool chip name', 'transistor_count': 10000000}
    assert result[0] == expected_res


def test_get_specific_component_s1():
    results = get_specific_component_s("cpu", {'transistor_count__gt': 9000000000})
    expected_res = list
    assert isinstance(results, expected_res)
    assert results != []


def test_get_specific_component_s2():
    with pytest.raises(ValueError):
        bad_collection = "bad"
        get_specific_component_s(bad_collection, {'transistor_count__gt': 9000000000})


def test_get_specific_component_s3():
    result = get_specific_component_s("cpu")
    expected_res = get_a_collection("cpu")
    assert result == expected_res


def test_add_data():
    component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                      'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", component_data)
    expected_res = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                    'processor': 'cool chip name', 'transistor_count': 10000000}
    results = get_specific_component_s("cpu", component_data)[0]
    assert expected_res == results


def test_add_data1():
    component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                      'processor': 'cool chip name', 'transistor_count': 10000000}
    cpu1 = make_dict_to_obj(component_data)
    add_data("cpu", cpu1)
    results = get_specific_component_s("cpu", component_data)[0]
    assert results == component_data


def test_add_data2(capsys):
    component_data = {"bad": "data"}
    add_data("cpu", component_data)
    captured = capsys.readouterr()
    assert """{'error': 'data not in correct format', 'expected_keys': ['processor', 'transistor_count', 'date_of_introduction', 'designer', 'process', 'area'], 'received_keys': ['bad']}""" in captured.out


def test_add_data3():
    with pytest.raises(ValueError):
        component_data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                          'processor': 'cool chip name', 'transistor_count': 10000000}
        add_data("bad", component_data)


def test_add_data4():
    with pytest.raises(ValueError):
        bad_col_name = "bad"
        add_data(bad_col_name, {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
                                'processor': 'cool chip name', 'transistor_count': 10000000})


def test_add_data5(capsys):
    add_data("gpu", {})
    captured = capsys.readouterr()
    assert "{'error': 'No data provided'}" in captured.out


def test_add_data6(capsys):
    data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
            'processor': 'cool chip name', 'transistor_count': 10000000}
    delete_component_s("cpu", data)
    add_data("cpu", data)
    add_data("cpu", data)
    captured = capsys.readouterr()
    assert "{'error': 'data already present'}\n" in captured.out


def test_add_many(capsys):
    data = [{'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 10, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 100, 'date_of_introduction': 1870, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000}]
    delete_component_s("cpu", {'designer': 'cool designer'})
    add_many("cpu", data)
    captured = capsys.readouterr()
    assert "{'message': 'data inserted successfully'}" in captured.out


def test_add_many1():
    with pytest.raises(ValueError):
        data = []
        add_many("cpu", data)


def test_add_many2():
    with pytest.raises(ValueError):
        add_many("bad", [])


def test_update_a_component(capsys):
    data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100, 'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", data)
    update_a_component("cpu", data, data={'date_of_introduction': 1971})
    captured = capsys.readouterr()
    assert "{'message': 'updated one component'}" in captured.out


def test_update_a_component1(capsys):
    data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100, 'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", data)
    update_a_component("cpu", data, data={})
    captured = capsys.readouterr()
    assert "{'error': 'No data provided'}" in captured.out


def test_update_a_component2(capsys):
    data = {"invalid": "data"}
    add_data("cpu", data)
    update_a_component("cpu", data, data={'area': 100})
    captured = capsys.readouterr()
    assert "{'error': 'data not in correct format', 'expected_keys': ['processor', 'transistor_count', 'date_of_introduction', 'designer', 'process', 'area'], 'received_keys': ['invalid']}" in captured.out


def test_update_a_component3(capsys):
    with pytest.raises(ValueError):
        data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100, 'processor': 'cool chip name', 'transistor_count': 10000000}
        add_data("bad", data)


def test_delete_component_s(capsys):
    data = {'area': 100, 'date_of_introduction': 1970, 'designer': 'cool designer', 'process': 100,
            'processor': 'cool chip name', 'transistor_count': 10000000}
    add_data("cpu", data)
    delete_component_s("cpu", data)
    captured = capsys.readouterr()
    assert "{'message': 'removed 1 component(s)'}" in captured.out


def test_delete_component_s1(capsys):
    data = [{'area': 100, 'date_of_introduction': 1, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 10, 'date_of_introduction': 2, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000},
            {'area': 100, 'date_of_introduction': 3, 'designer': 'cool designer', 'process': 100,
             'processor': 'cool chip name', 'transistor_count': 10000000}]
    add_many("cpu", data)
    delete_component_s("cpu", {'date_of_introduction__lt': 5})
    captured = capsys.readouterr()
    assert "{'message': 'removed 3 component(s)'}" in captured.out


def test_delete_component_s2(capsys):
    # run add data to mongo script
    delete_component_s("ram", {})
    captured = capsys.readouterr()
    assert "{'message': 'removed collection ram'}" in captured.out


def test_delete_component_s3():
    with pytest.raises(ValueError):
        delete_component_s("ram", {})
        delete_component_s("ram", {})


def test_delete_component_s4():
    with pytest.raises(ValueError):
        delete_component_s("bad", {'date_of_introduction__lt': 5})


def test_delete_collection():
    with pytest.raises(ValueError):
        delete_component_s("gpu")
        get_a_collection("gpu")


def test_delete_collection1():
    with pytest.raises(ValueError):
        delete_component_s("bad")


def test_plot_components():
    with pytest.raises(ValueError):
        plot_components("cpu", "bad")


def test_plot_components1():
    with pytest.raises(ValueError):
        plot_components(["bad", "worse", "cpu"], feature="transistor_count")


