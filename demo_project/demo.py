from web_client.main import *
from web_client.turn_dict_to_obj import *

# shows all the different functionalities of the client library
# remember to get the main from the client library as a package and not form the local directory

# from client_package.web_client.main import *
# from client_package.web_client.turn_dict_to_obj import *


if __name__ == '__main__':

    # home message

    home_message = home_message()
    authors = home_message["authors"]
    print(f"Authors: {authors}")
    str_1 = "The methods that this library offers are: \n"
    for method in home_message["methods"]:
        str_1 += f"\t-{method}\n"
    print(str_1)

    # what collections are there

    print(f"Available collections: {get_component_names()}\n")

    # what are the features of the ram collection

    collection_names = get_component_names()
    str_2 = ""
    for col in collection_names:
        str_2 += f"The {col} has features: {get_components_features(col)}\n"
    print(str_2)

    # let's get a collection of gpus

    gpus = get_a_collection("gpu")

    # let's make them into GPU objects

    gpu_objs = make_list_of_dict_to_obj(gpus)

    print("Example of gpu object:")
    print(gpu_objs[0])

    # what are the gpu features representing

    print(gpu_objs[0].describe_component_features())

    # let's create a new cpu
    # they are automatically already added to the database

    new_cpu = Cpu(processor="new cool cpu", transistor_count=10000000, area=15, date_of_introduction=2025, designer="cool company", process=10)
    new_cpu1 = Cpu(processor="new cool cpu1", transistor_count=10000000, area=15, date_of_introduction=2025, designer="cool company", process=10)

    print(new_cpu)

    # let's change a feature value

    new_cpu1.transistor_count = 50000000

    print(new_cpu1)

    # let's find all ram chips made after or in 2015

    ram_features = {"date_of_introduction__gte": 2015}
    ram_chips = get_specific_component_s("ram", ram_features)

    print(ram_chips)

    ram_chip_1980_obj = make_list_of_dict_to_obj(ram_chips)

    # let's get the latest year of introduction

    latest_year = 0
    latest_ram = None
    for ram in ram_chip_1980_obj:
        if ram.year_of_introduction > latest_year:
            latest_year = ram.year_of_introduction
            latest_ram = ram

    print(f"Latest year of ram in our dataset: {latest_year}")
    print(latest_ram)

    # let's add some newer rams

    ram = Ram("LPDDR4", 1200, 2018, 120, 10, "Mb", 8192, "SK Hynix", "LPDDR4")

    rams = [{'area': 200, 'bit_units': "GB", 'capacity_bits': 32768, 'chip_name': "DDR5", 'date_of_introduction': 2019,
             'manufacturer_s': "G.Skill", 'process': 7, 'ram_type': "DDR5", 'transistor_count': 3000},
            {'area': 250, 'bit_units': "GB", 'capacity_bits': 16384, 'chip_name': "DDR5", 'date_of_introduction': 2020,
             'manufacturer_s': "Corsair", 'process': 10, 'ram_type': "DDR5", 'transistor_count': 1000}]

    add_many("ram", rams)

    # we can update just by finding the component, no need to convert it into an object if you don't want to
    # let's update one

    update_a_component("ram", {"chip_name": "LPDDR4", "date_of_introduction": 2018}, {"area": 125})

    # let's delete components with NA in transistor count

    for component in get_component_names():
        delete_component_s(component, {"transistor_count": "NA"})

    # finally, let's plot all the components with their transistor count
    # or if we want to only plot a singular component, we can do so

    plot_components(["cpu", "gpu", "ram"], "transistor_count", logged=True)
