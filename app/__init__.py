from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from app.models.session_storage import Base, DBSession
import config

sql_config = {'db.url': config.SQLITE_DB , 'db.echo': 'True'}
engine = engine_from_config(sql_config, prefix="db.")
DBSession.configure(bind=engine)
Base.metadata.create_all(engine)

config = Configurator()
config.include('pyramid_chameleon')
session_factory = SignedCookieSessionFactory("itsaseekreet")
config.set_session_factory(session_factory)

config.scan()

app = config.make_wsgi_app()


