class Restaurant:
    def __init__(self, name):
        self._name = self._validate_name(name)
        self._reviews = []

    @property
    def name(self):
        return self._name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1:
            raise ValueError("Name must have at least 1 character")
        return name

    def reviews(self):
        return self._reviews

    def customers(self):
        return list({review.customer for review in self._reviews})

    def average_star_rating(self):
        if not self._reviews:
            return None
        return round(sum(review.rating for review in self._reviews) / len(self._reviews), 1)

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(cls.all(), key=lambda restaurant: restaurant.average_star_rating() or 0, reverse=True)
        return sorted_restaurants[:2]
