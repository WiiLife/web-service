from client_package.web_client.component import Component
from client_package.web_client.main import update_a_component, add_data, get_specific_component_s


class Ram(Component):
    def __init__(self, chip_name: str, transistor_count: int, date_of_introduction: int, area: int, process: int,
                 bit_units: str, capacity_bits: int, manufacturer_s: str, ram_type: str):
        super().__init__(chip_name, transistor_count, date_of_introduction, area, process)

        self.__bit_units = bit_units
        self.__capacity_bits = capacity_bits
        self.__manufacturer_s = manufacturer_s
        self.__ram_type = ram_type

        component_data = {"chip_name": self.processor_name,
                          "transistor_count": self.transistor_count,
                          "date_of_introduction": self.year_of_introduction,
                          "area": self.area,
                          "process": self.process,
                          "manufacturer_s": self.__manufacturer_s,
                          "bit_units": self.__bit_units,
                          "capacity_bits": self.__capacity_bits,
                          "ram_type": self.__ram_type}

        if not get_specific_component_s("ram", component_data):
            add_data("ram", component_data)

    def _update_comp(self, feature, value):
        # updates the component with new feature
        update_a_component("ram", {"chip_name": self.processor_name,
                                   "transistor_count": self.transistor_count,
                                   "date_of_introduction": self.year_of_introduction,
                                   "area": self.area,
                                   "process": self.process,
                                   "manufacturer_s": self.__manufacturer_s,
                                   "bit_units": self.__bit_units,
                                   "capacity_bits": self.__capacity_bits,
                                   "ram_type": self.__ram_type},
                           {feature: value})

    @Component.transistor_count.setter
    def transistor_count(self, value):

        if value >= 0:
            self._update_comp("transistor_count", value)
            self._Component__transistor_count = value

        else:
            raise ValueError(f"transistor count has to be > 0, not {value}")

    @Component.processor_name.setter
    def processor_name(self, value: str):
        self._update_comp("chip_name", value)
        self._Component__processor_name = value

    @Component.year_of_introduction.setter
    def year_of_introduction(self, value: int):

        if value > 0:
            self._update_comp("date_of_introduction", value)
            self._Component__year_of_introduction = value

        else:
            raise ValueError(f"year_of_introduction has to be > 0, not {value}")

    @Component.area.setter
    def area(self, value: int):

        if value > 0:
            self._update_comp("area", value)
            self._Component__area = value

        else:
            raise ValueError(f"area has to be > 0, not {value}")

    @Component.process.setter
    def process(self, value: int):

        if value > 0:
            self._update_comp("process", value)
            self._Component__process = value

        else:
            raise ValueError(f"process has to be > 0, not {value}")

    @property
    def bit_units(self):
        return self.__bit_units

    @bit_units.setter
    def bit_units(self, value: int):
        self._update_comp("bit_units", value)
        self.__bit_units = value

    @property
    def capacity_bits(self):
        return self.__capacity_bits

    @capacity_bits.setter
    def capacity_bits(self, value):
        if value > 0:
            self._update_comp("capacity_bits", value)
            self.__capacity_bits = value

        else:
            raise ValueError(f"capacity_bits has to be > 0, not {value}")

    @property
    def manufacturer(self):
        return self.__manufacturer_s

    @manufacturer.setter
    def manufacturer(self, value: str):
        self._update_comp("manufacturer_s", value)
        self.__manufacturer_s = value

    @property
    def ram_type(self):
        return self.__ram_type

    @ram_type.setter
    def ram_type(self, value: str):
        self._update_comp("ram_type", value)
        self.__ram_type = value

    def __repr__(self):
        str_out = Component.__repr__(self)
        str_out += f"""|manufacturer           |{self.__manufacturer_s}	 
|bit units              |{self.__bit_units}
|capacity units         |{self.__capacity_bits}
|ram type               |{self.__ram_type}
        """
        return str_out

    def describe_component_features(self):
        out_str = """
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
        return out_str

    def get_dict(self):
        component_data = {"chip_name": self.processor_name,
                          "transistor_count": self.transistor_count,
                          "date_of_introduction": self.year_of_introduction,
                          "area": self.area,
                          "process": self.process,
                          "manufacturer_s": self.__manufacturer_s,
                          "bit_units": self.__bit_units,
                          "capacity_bits": self.__capacity_bits,
                          "ram_type": self.__ram_type}

        return component_data
