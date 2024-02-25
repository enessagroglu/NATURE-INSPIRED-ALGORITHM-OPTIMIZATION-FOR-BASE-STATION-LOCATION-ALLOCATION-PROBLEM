
class BaseStation:
    def __init__(self, type, coordinate, current_usage):
        self.__type = type
        self.__coordinate = coordinate
        self.__range = range

    def get_type(self):
        return self.__type

    def get_coordinate(self):
        return self.__coordinate

    def get_range(self):
        return self.__range
    
    def get_current_usage(self):
        return self.__current_usage

    def set_type(self, type):
        self.__type = type

    def set_coordinate(self, coordinate):
        self.__coordinate = coordinate

    def set_range(self, range):
        self.__range = range
    
    def set_current_usage(self, current_usage):
        self.__current_usage = current_usage

    def __str__(self):
        return f"Type: {self.__type}, Coordinate: {self.__coordinate}, Capacity: {self.__type.capacity}, Current Usage: {self.__current_usage}"

class Type:
    def __init__(self, name, speed, frequency):
        self.__name = name
        self.__speed = speed
        self.__frequency = frequency

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_frequency(self):
        return self.__frequency

    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_frequency(self, frequency):
        self.__frequency = frequency

    def __str__(self):
        return f"Type: {self.__name}, Speed: {self.__speed}, Frequency: {self.__frequency}"
