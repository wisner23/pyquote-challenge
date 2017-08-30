from resources.quotes import quotes


class QuoteService(object):

    def __init__(self, randomizer):
        self.rdn = randomizer

    @staticmethod
    def get_quotes():
        """
            Metodo no qual retorna uma lista de quotes
            :return: array[]
            """
        return quotes

    @staticmethod
    def get_quote_by_number(number):
        """
            Metodo no qual recebe um numero como parametro e utiliza o mesmo como indice
            para obter o resultado da lista quotes.

            :param number: int value
            :return: a quote {}
            """
        return quotes[number]

    def get_random_quote(self):
        """
            Metodo no qual randomiza um inteiro do tamanho de quotes e utiliza o mesmo como indice
            para obter um  da lista quotes.

            :param number: int value
            :return: a quote {}
            """
        return self.get_quote_by_number(self.rdn(0, len(quotes) - 1))
