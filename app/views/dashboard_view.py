from pyramid.view import view_config

from app.services.dashboard_service import DashboardService

dashboard_service = DashboardService()


@view_config(route_name="dashboard", renderer="json")
def get_dashboard(request):
    """
    Este metodo ira receber uma requisicao e buscar no banco, todos os logs de sessao
    ira converter para um view model atraves do metodo map_to_dashboard() e retornar um json
    :param request:
    :return: a json object
    """
    result = [map_to_dashboard(log) for log in dashboard_service.get_dashboard()]
    return {"data": result}


def map_to_dashboard(log):
    """
    Este metodo recebe um objeto do tipo SessionStorage e retorna um View Model
    :param log: SessionStorage
    :return: { session_id, servico, data }
    """
    return {
        "session_id": log.session_id,
        "serviço": log.service_name,
        "data": "{:%d/%m/%Y %H:%M:%S}".format(log.date)
    }
