from random import randint
from pyramid.view import view_config
from app.services.quote_service import QuoteService
from app.services.session_logging_service import logging_session
import requests

quote_service = QuoteService(randint, requests)


@view_config(route_name="quotes", renderer="app.views:templates/quotes.pt", decorator=logging_session)
def get_quotes(request):
    """
        View que recebe um request do tipo GET e retorna todos os Quotes em bullet points
        :param  request: requisiçao enviada pelo caller

        :return lista de quote

        GET /quotes
    """
    return {"quotes": quote_service.get_quotes()}


@view_config(route_name="quote", renderer="app.views:templates/quote.pt", decorator=logging_session)
def get_quote_by_number(request):
    """
        View que recebe um request do tipo GET passando um numero e retorna o
        um quote de acordo com o numero fornecido.

        :param number: essa requisiçao devera ter um numero passado como parametro
        :param request: requisiçao enviada pelo caller

        :return quote

        GET /quote/1
    """
    id = request.matchdict["number"]
    quote = quote_service.get_quote_by_number(id)
    return quote


@view_config(route_name="random_quote", renderer="app.views:templates/quote_random.pt", decorator=logging_session)
def get_random_quote(request):
    """
        View que recebe um request do tipo GET passando um numero e retorna o
        um quote de acordo com o numero fornecido.

        GET /quote/1
    """
    return quote_service.get_random_quote()
