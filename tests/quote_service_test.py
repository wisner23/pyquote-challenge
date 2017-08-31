import unittest
from tests.resources.quotes import quotes
from app.services.quote_service import QuoteService
from tests import request_stub


class QuoteServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.quote_service = QuoteService(cls.mock_random_value, request_stub)

    def test_should_return_a_list(self):
        q = quotes
        x = self.quote_service.get_quotes()
        self.assertListEqual(q, x)

    def test_should_return_a_quote(self):
        number = 2
        current_result = self.quote_service.get_quote_by_number(number)
        expected_result = {"quote": quotes[number]}

        self.assertEqual(expected_result, current_result)

    def test_should_return_a_random_quote(self):
        current_result = self.quote_service.get_random_quote()

        expected_result = {"sorted_number": self.mock_random_value(1, 2), "quote": current_result["quote"]}
        self.assertEqual(expected_result, current_result)

    @staticmethod
    def mock_random_value(param1, param2):
        return 2
