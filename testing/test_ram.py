import pytest
from web_client.ram import Ram
from web_client.main import get_specific_component_s

# temporary
# from client_package.web_client.ram import Ram
# from client_package.web_client.main import get_specific_component_s


def get_comp_results(ram: Ram):
    result = get_specific_component_s("ram", {
        "chip_name": ram.processor_name,
        "transistor_count": ram.transistor_count,
        "date_of_introduction": ram.year_of_introduction,
        "area": ram.area,
        "process": ram.process,
        "manufacturer_s": ram.manufacturer,
        "bit_units": ram.bit_units,
        "capacity_bits": ram.capacity_bits,
        "ram_type": ram.ram_type
    })[0]
    return result


def test_ram_init():
    ram = Ram("DDR5", 1000, 2020, 250, 10, "Gb", 16384, "Corsair", "DDR5")
    result = get_comp_results(ram)
    for key in ram.get_dict().keys():
        assert result[key] == ram.get_dict()[key]


def test_ram_transistor_count():
    ram = Ram("DDR5", 1000, 2020, 250, 10, "Gb", 16384, "Corsair", "DDR5")
    ram.transistor_count = 9999
    result = get_comp_results(ram)
    assert ram.transistor_count == result["transistor_count"]


def test_ram_transistor_count_invalid():
    ram = Ram("DDR5", 1000, 2020, 250, 10, "Gb", 16384, "Corsair", "DDR5")
    with pytest.raises(ValueError):
        ram.transistor_count = -100


def test_processor_name_setter():
    ram = Ram("DDR4", 2000, 2015, 100, 22, "Mb", 8192, "Samsung", "DDR4")
    ram.processor_name = "LPDDR5X"
    result = get_comp_results(ram)
    assert ram.processor_name == result["chip_name"]


def test_year_of_introduction_valid():
    ram = Ram("DDR5", 3000, 2019, 200, 7, "Gb", 32768, "G.Skill", "DDR5")
    ram.year_of_introduction = 2022
    result = get_comp_results(ram)
    assert ram.year_of_introduction == result["date_of_introduction"]


def test_year_of_introduction_invalid():
    ram = Ram("DDR5", 3000, 2019, 200, 7, "Gb", 32768, "G.Skill", "DDR5")
    with pytest.raises(ValueError):
        ram.year_of_introduction = 0


def test_area_setter_valid():
    ram = Ram("DDR3", 1500, 2010, 180, 22, "Mb", 4096, "Kingston", "DDR3")
    ram.area = 400
    result = get_comp_results(ram)
    assert ram.area == result["area"]


def test_area_setter_invalid():
    ram = Ram("DDR3", 1500, 2010, 180, 22, "Mb", 4096, "Kingston", "DDR3")
    with pytest.raises(ValueError):
        ram.area = -20


def test_process_setter_valid():
    ram = Ram("DDR4", 2000, 2016, 140, 14, "Gb", 16384, "Micron", "DDR4")
    ram.process = 5
    result = get_comp_results(ram)
    assert ram.process == result["process"]


def test_process_setter_invalid():
    ram = Ram("DDR4", 2000, 2016, 140, 14, "Gb", 16384, "Micron", "DDR4")
    with pytest.raises(ValueError):
        ram.process = 0


def test_bit_units_setter():
    ram = Ram("LPDDR4", 1200, 2018, 120, 10, "Mb", 8192, "SK Hynix", "LPDDR4")
    ram.bit_units = "Gb"
    result = get_comp_results(ram)
    assert ram.bit_units == result["bit_units"]


def test_capacity_bits_setter():
    ram = Ram("LPDDR4", 1200, 2018, 120, 10, "Mb", 8192, "SK Hynix", "LPDDR4")
    ram.capacity_bits = 65536
    result = get_comp_results(ram)
    assert ram.capacity_bits == result["capacity_bits"]


def test_capacity_bits_invalid():
    ram = Ram("LPDDR4", 1200, 2018, 120, 10, "Mb", 8192, "SK Hynix", "LPDDR4")
    with pytest.raises(ValueError):
        ram.capacity_bits = -100


def test_manufacturer_setter():
    ram = Ram("DDR3", 1400, 2012, 170, 20, "Mb", 4096, "OldManu", "DDR3")
    ram.manufacturer = "NewManu"
    result = get_comp_results(ram)
    assert ram.manufacturer == result["manufacturer_s"]


def test_ram_type_setter():
    ram = Ram("SomeChip", 500, 2008, 90, 32, "Mb", 2048, "Generic", "OldType")
    ram.ram_type = "UpdatedType"
    result = get_comp_results(ram)
    assert ram.ram_type == result["ram_type"]


def test_describe_component_features():
    ram = Ram("TestRam", 100, 2000, 10, 45, "Gb", 1024, "TestManu", "TestType")
    output = ram.describe_component_features()
    expected_output = """
_________________________________________________________________________________
|variable	            |class	    |description                                  |
|-----------------------|-----------|---------------------------------------------|
|chip_name	            |string  	|chip name                                    |
|capacity_bits          |integer    |how many units of information it can work on |
|transistor_count	    |integer    |Number of transistors                        |
|bit_units              |string     |Units for bit capacity (bits < kb < Mb < Gb) |
|ram_type               |string     |Ram type                                     |
|date_of_introduction	|integer	|year introduced                              |
|designer	            |string 	|Designer                                     |
|process	            |integer    |Size of manufacturing process (in nanometers)|
|area	                |integer	|Area of chip in square millimeters           |
|manufacturer_s         |string     |manufacturer(s)                              |
_________________________________________________________________________________
        """
    assert output == expected_output


def test_get_dict():
    ram = Ram("DDR5", 1000, 2020, 250, 10, "Gb", 16384, "Corsair", "DDR5")
    result = get_comp_results(ram)
    assert ram.get_dict() == result
