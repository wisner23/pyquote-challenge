import config
from app.common.api_exception import ApiException


class QuoteService(object):

    def __init__(self, randomizer, request):
        self.rdn = randomizer
        self.request = request

    def get_quotes(self):
        """
        Metodo no qual realiza uma consulta na API de quotes e retorna uma lista de quotes
        :return: array[]
        """
        try:
            return self.request.get(config.API_ENDPOINT).json()["quotes"]
        except:
            raise ApiException("API is not available: __get_quotes__")

    def get_quote_by_number(self, number):
        """
        Metodo no qual recebe um numero como parametro e realiza uma consulta na API de quotes
        passando o numero

        :param number: number of requested quote
        :return: a quote {}
        """
        try:
            url = "{0}/{1}".format(config.API_ENDPOINT, number)
            result = self.request.get(url)
            return result.json()
        except:
            raise ApiException("API is not available: __get_quote_by_number__")

    def get_random_quote(self):
        """
        Metodo no qual randomiza um inteiro do tamanho de quotes e utiliza o metodo get_quote_by_number
        para obter um retorno

        :return: a quote {}
        """
        sorted_number = self.rdn(0, len(self.get_quotes()) - 1)
        result = self.get_quote_by_number(sorted_number)

        return {"sorted_number": sorted_number, "quote": result["quote"]}
