from customer import Customer
from restaurant import Restaurant



class Review:
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = self._validate_rating(rating)
        self._customer.add_review(self)
        self._restaurant.add_review(self)

    @property
    def rating(self):
        return self._rating

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        if not isinstance(new_customer, Customer):
            raise ValueError("Customer must be of type 'Customer'")
        self._customer.reviews().remove(self)
        self._customer = new_customer
        self._customer.add_review(self)

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, new_restaurant):
        if not isinstance(new_restaurant, Restaurant):
            raise ValueError("Restaurant must be of type 'Restaurant'")
        self._restaurant.reviews().remove(self)
        self._restaurant = new_restaurant
        self._restaurant.add_review(self)

    def _validate_rating(self, rating):
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating
