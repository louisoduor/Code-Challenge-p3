from review import Review

class Customer:
    def __init__(self, first_name, last_name):
        self._first_name = self._validate_name(first_name)
        self._last_name = self._validate_name(last_name)
        self._reviews = []

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 1 <= len(name) <= 25:
            raise Exception("Name must be between 1 and 25 characters")
        return name

    def reviews(self):
        return self._reviews

    def restaurants(self):
        return list({review.restaurant for review in self._reviews})

    def num_negative_reviews(self):
        return sum(1 for review in self._reviews if review.rating <= 2)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self._reviews)

    # New methods:

    def add_review(self, review):
        if not isinstance(review, Review):
            raise ValueError("Review must be of type 'Review'")
        self._reviews.append(review)

    def remove_review(self, review):
        if review in self._reviews:
            self._reviews.remove(review)
        else:
            raise ValueError("Review not found")

    def clear_reviews(self):
        self._reviews = []

