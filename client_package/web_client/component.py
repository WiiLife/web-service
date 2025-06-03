from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name: str, transistor_count: int, date_of_introduction: int, area: int, process: int):

        # common features for all chips
        self.__transistor_count = transistor_count
        self.__processor_name = name
        self.__year_of_introduction = date_of_introduction
        self.__area = area
        self.__process = process

    @property
    def transistor_count(self):
        return self.__transistor_count

    @transistor_count.setter
    @abstractmethod
    def transistor_count(self, value):
        pass

    @property
    def processor_name(self):
        return self.__processor_name

    @processor_name.setter
    @abstractmethod
    def processor_name(self, value: str):
        pass

    @property
    def year_of_introduction(self):
        return self.__year_of_introduction

    @year_of_introduction.setter
    @abstractmethod
    def year_of_introduction(self, value: int):
        pass

    @property
    def area(self):
        return self.__area

    @area.setter
    @abstractmethod
    def area(self, value):
        pass

    @property
    def process(self):
        return self.__process

    @process.setter
    @abstractmethod
    def process(self, value: int):
        pass

    def __repr__(self):
        return f"""
|processor name         |{self.__processor_name}
|year of introduction   |{self.__year_of_introduction}
|transistor count       |{self.__transistor_count}                                 
|chip area (nm)	        |{self.__area}                                
|process            	|{self.__process}	                             
"""

    @abstractmethod
    def describe_component_features(self) -> str:
        pass

    # add methods that are collective for all components to use polymorphism

    @abstractmethod
    def get_dict(self):
        pass
