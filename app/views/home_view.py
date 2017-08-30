from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="home")
def get_home(request):
    """
    Apresenta  pagina inicial
    """
    return Response("<h1>Desafio Web 1.0</h1>")