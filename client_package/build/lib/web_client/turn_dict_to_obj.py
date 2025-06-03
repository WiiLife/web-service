from client_package.web_client.cpu import Cpu
from client_package.web_client.gpu import Gpu
from client_package.web_client.ram import Ram
from client_package.web_client.component import Component
from client_package.web_client.main import get_components_features


def make_dict_to_obj(data: dict) -> Component:

    if list(data.keys()) == get_components_features("cpu"):
        return Cpu(data["processor"], data["transistor_count"], data["date_of_introduction"], data["area"], data["process"], data["designer"])

    if list(data.keys()) == get_components_features("gpu"):
        return Gpu(data["processor"], data["transistor_count"], data["date_of_introduction"], data["area"], data["process"], data["designer_s"], data["manufacturer_s"])

    if list(data.keys()) == get_components_features("ram"):
        return Ram(data["chip_name"], data["transistor_count"], data["date_of_introduction"], data["area"], data["process"], data["bit_units"], data["capacity_bits"], data["manufacturer_s"], data["ram_type"])


def make_list_of_dict_to_obj(list_dict: list[dict]) -> list[Component]:
    all_comp = []
    for comp_data in list_dict:
        all_comp.append(make_dict_to_obj(comp_data))

    return all_comp
