import pytest
from web_client.cpu import Cpu
from web_client.main import get_specific_component_s

# temporary
# from client_package.web_client.cpu import Cpu
# from client_package.web_client.main import get_specific_component_s


def get_comp_results(cpu: Cpu):
    result = get_specific_component_s("cpu", {"processor": cpu.processor_name,
                                              "transistor_count": cpu.transistor_count,
                                              "date_of_introduction": cpu.year_of_introduction,
                                              "area": cpu.area,
                                              "process": cpu.process,
                                              "designer": cpu.designer})[0]
    return result


def test_cpu_init():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    result = get_comp_results(cpu)
    for key in cpu.get_dict().keys():
        assert result[key] == cpu.get_dict()[key]


def test_cpu_transistor_count():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.transistor_count = 10
    results = get_comp_results(cpu)

    assert cpu.transistor_count == results["transistor_count"]


def test_cpu_transistor_count1():
    with pytest.raises(ValueError):
        cpu = Cpu("one", 1, 2, 3, 4, "two")
        cpu.transistor_count = -1


def test_processor_name_setter():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.processor_name = "Intel i7"
    results = get_comp_results(cpu)
    assert cpu.processor_name == results["processor"]


def test_year_of_introduction_setter_valid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.year_of_introduction = 2020
    results = get_comp_results(cpu)
    assert cpu.year_of_introduction == results["date_of_introduction"]


def test_year_of_introduction_setter_invalid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    with pytest.raises(ValueError):
        cpu.year_of_introduction = -1


def test_area_setter_valid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.area = 50
    results = get_comp_results(cpu)
    assert cpu.area == results["area"]


def test_area_setter_invalid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    with pytest.raises(ValueError):
        cpu.area = 0


def test_process_setter_valid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.process = 10
    results = get_comp_results(cpu)
    assert cpu.process == results["process"]


def test_process_setter_invalid():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    with pytest.raises(ValueError):
        cpu.process = -5


def test_designer_setter():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    cpu.designer = "lili lala"
    results = get_comp_results(cpu)
    assert cpu.designer == results["designer"]


def test_describe_component():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    results = cpu.describe_component_features()
    expected_results = """
 _________________________________________________________________________________
|variable	            |class	    |description                                  |
|-----------------------|-----------|---------------------------------------------|
|processor	            |string  	|Processor name                               |
|transistor_count	    |integer    |Number of transistors                        |
|date_of_introduction	|integer	|year introduced                              |
|designer	            |string 	|Designer                                     |
|process	            |integer    |Size of manufacturing process (in nanometers)|
|area	                |integer	|Area of chip in square millimeters           |
 _________________________________________________________________________________
        """
    assert results == expected_results


def test_get_dict():
    cpu = Cpu("one", 1, 2, 3, 4, "two")
    results = get_comp_results(cpu)

    assert cpu.get_dict() == results

