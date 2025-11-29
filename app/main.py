from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: float, brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: float = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        if distance_from_city_center <= 0:
            raise ValueError("distance_from_city_center must be > 0")

        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: float = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        difference = max(self.clean_power - car.clean_mark, 0)
        cost = (car.comfort_class * difference * self.average_rating) / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float:
        cost = self.calculate_washing_price(car)
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return cost

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            income += self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: float) -> float:
        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1)) + rate)
            / self.count_of_ratings,
            1,
        )
        return self.average_rating
