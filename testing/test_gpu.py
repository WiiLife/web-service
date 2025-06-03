import pytest
from web_client.gpu import Gpu
from web_client.main import get_specific_component_s

# temporary
# from client_package.web_client.gpu import Gpu
# from client_package.web_client.main import get_specific_component_s


def get_comp_results(gpu: Gpu):
    result = get_specific_component_s("gpu", {
        "processor": gpu.processor_name,
        "transistor_count": gpu.transistor_count,
        "date_of_introduction": gpu.year_of_introduction,
        "area": gpu.area,
        "process": gpu.process,
        "designer_s": gpu.designer,
        "manufacturer_s": gpu.manufacturer
    })[0]
    return result


def test_gpu_init():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    result = get_comp_results(gpu)
    for key in gpu.get_dict().keys():
        assert result[key] == gpu.get_dict()[key]


def test_gpu_transistor_count():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.transistor_count = 10
    results = get_comp_results(gpu)
    assert gpu.transistor_count == results["transistor_count"]


def test_gpu_transistor_count_invalid():
    with pytest.raises(ValueError):
        gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
        gpu.transistor_count = -1


def test_processor_name_setter():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.processor_name = "NVIDIA RTX 3080"
    results = get_comp_results(gpu)
    assert gpu.processor_name == results["processor"]


def test_year_of_introduction_setter_valid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.year_of_introduction = 2021
    results = get_comp_results(gpu)
    assert gpu.year_of_introduction == results["date_of_introduction"]


def test_year_of_introduction_setter_invalid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    with pytest.raises(ValueError):
        gpu.year_of_introduction = -1


def test_area_setter_valid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.area = 100
    results = get_comp_results(gpu)
    assert gpu.area == results["area"]


def test_area_setter_invalid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    with pytest.raises(ValueError):
        gpu.area = 0


def test_process_setter_valid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.process = 7
    results = get_comp_results(gpu)
    assert gpu.process == results["process"]


def test_process_setter_invalid():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    with pytest.raises(ValueError):
        gpu.process = -5


def test_designer_setter():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.designer = "New Designer"
    results = get_comp_results(gpu)
    assert gpu.designer == results["designer_s"]


def test_manufacturer_setter():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    gpu.manufacturer = "New Manufacturer"
    results = get_comp_results(gpu)
    assert gpu.manufacturer == results["manufacturer_s"]


def test_describe_component():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    results = gpu.describe_component_features()
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
|manufacturer           |string     |manufacturer(s)                              |
_________________________________________________________________________________
        """
    assert results == expected_results


def test_get_dict():
    gpu = Gpu("one", 1, 2, 3, 4, "designer1", "manufacturer1")
    results = get_comp_results(gpu)
    assert gpu.get_dict() == results
