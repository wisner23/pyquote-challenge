from app.models import session_storage

db = session_storage.DBSession


class DashboardService(object):

    @staticmethod
    def get_dashboard():
        """
        Este metodo ira buscar todos registros de logging no banco e ira retornar
        :return: SessionStorage -> list
        """
        return db.query(session_storage.SessionStorage).all()
