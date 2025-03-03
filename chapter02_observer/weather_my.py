
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


@dataclass
class WeatherData(Subject):
    temperature: float = None
    humidity: float = None
    pressure: float = None
    observers: list = field(default_factory=list)

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

@dataclass
class CurrentConditionsDisplay(DisplayElement, Observer):
    _weather_data: WeatherData

    def __post_init__(self):
        self._temperature: float = None  
        self._humidity: float = None
        self._pressure: float = None

        self._weather_data.register_observer(self)

    def display(self):
        print(
            f"Current conditions: "
            f"{self._temperature:.1f}F degrees and "
            f"{self._humidity:.1f}% humidity"
        )

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self.display()
    


@dataclass
class StatisticsDisplay(DisplayElement, Observer):
    _weather_data: WeatherData

    def __post_init__(self):
        self._max_temp: float = 0.
        self._min_temp: float = 200.
        self._temp_sum: float = 0.
        self._num_readings: int = 0
        self._weather_data.register_observer(self)


    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1
        self._max_temp = max(temp, self._max_temp)
        self._min_temp = min(temp, self._min_temp)
        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = "
              f"{self._temp_sum / self._num_readings}"
              f"/{self._max_temp}"
              f"/{self._min_temp}"
              )

def weather_station():

    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

if __name__ == '__main__':
    weather_station()
