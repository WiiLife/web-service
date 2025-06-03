from client_package.web_client.component import Component
from client_package.web_client.main import update_a_component, add_data, get_specific_component_s


class Gpu(Component):
    def __init__(self, processor: str, transistor_count: int, date_of_introduction: int, area: int, process: int,
                 designer_s: str, manufacturer_s: str):
        super().__init__(processor, transistor_count, date_of_introduction, area, process)

        self.__designer_s = designer_s
        self.__manufacturer_s = manufacturer_s

        component_data = {"processor": self.processor_name,
                          "transistor_count": self.transistor_count,
                          "date_of_introduction": self.year_of_introduction,
                          "designer_s": self.__designer_s,
                          "manufacturer_s": self.__manufacturer_s,
                          "process": self.process,
                          "area": self.area
                          }

        if not get_specific_component_s("gpu", component_data):
            add_data("gpu", component_data)

    def _update_comp(self, feature, value):
        # updates the component with new feature
        update_a_component("gpu", {"processor": self.processor_name,
                                   "transistor_count": self.transistor_count,
                                   "date_of_introduction": self.year_of_introduction,
                                   "area": self.area,
                                   "process": self.process,
                                   "designer_s": self.__designer_s,
                                   "manufacturer_s": self.__manufacturer_s},
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
        self._update_comp("processor", value)
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
    def designer(self):
        return self.__designer_s

    @designer.setter
    def designer(self, value: str):
        self._update_comp("designer_s", value)
        self.__designer_s = value

    @property
    def manufacturer(self):
        return self.__manufacturer_s

    @manufacturer.setter
    def manufacturer(self, value: str):
        self._update_comp("manufacturer_s", value)
        self.__manufacturer_s = value

    def __repr__(self):
        str_out = Component.__repr__(self)
        str_out += f"""|designer            	|{self.__designer_s}	 
|manufacturer           |{self.__manufacturer_s}
        """
        return str_out

    def describe_component_features(self):
        out_str = """
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
        return out_str

    def get_dict(self):
        component_data = {"processor": self.processor_name,
                          "transistor_count": self.transistor_count,
                          "date_of_introduction": self.year_of_introduction,
                          "area": self.area,
                          "process": self.process,
                          "designer_s": self.__designer_s,
                          "manufacturer_s": self.__manufacturer_s}

        return component_data
