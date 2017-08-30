from app.models import session_storage
import uuid

db = session_storage.DBSession

def logging_session(view_callable):

    """
    Este decorator ira criar e guardar a sessao do usuario
    e a consulta realizada

    :param view_callable: view que sera chamada atraves do view_config
    :return: --
    """

    def wrapper(context, request):

        """
        Recebe o contexto da aplicaçao e o request.
        Verifica se o usuario ja possui uma sessao, caso nao possuir, ele cria uma nova
        Utilizando um uuid4 como indentificador da sessao, é salvo no banco a hora e a
        consulta realizada.

        :param context:  --
        :param request: --
        :return: --
        """

        session = request.session

        if "usersession" not in session:
            session["usersession"] = uuid.uuid4()

        model = session_storage.SessionStorage(str(session["usersession"]), view_callable.__name__)
        db.add(model)

        return view_callable(context, request)

    return wrapper
