class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        difference = max(self.clean_power - car.clean_mark, 0)
        cost = (car.comfort_class * difference * self.average_rating) / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car):
        cost = self.calculate_washing_price(car)
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return cost

    def serve_cars(self, cars: list[Car]):
        income = 0.0
        for car in cars:
            income += self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate):
        self.count_of_ratings += 1
        self.average_rating = round(((self.average_rating * (self.count_of_ratings - 1)) + rate) / self.count_of_ratings,1)
        return self.average_rating

