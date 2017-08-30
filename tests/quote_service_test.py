import unittest
from resources import quotes
from app.services.quote_service import QuoteService


class QuoteServiceTest(unittest.TestCase):

    def __init__(self):
        self.quote_service = QuoteService(self.mock_random_value)

    def should_return_a_list(self):
        self.assertListEqual(quotes, self.quote_service.get_quotes())

    def should_return_a_quote(self):
        number = 2
        self.assertEquals(quotes[number], self.quote_service.get_quote_by_number(number))

    def should_return_a_random_quote(self):
        self.assertEquals(quotes[2], self.quote_service.get_random_quote())

    @staticmethod
    def mock_random_value():
        return 2
