from sqlalchemy import Column, Integer, String, DateTime
import datetime
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension

metadata = MetaData()
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base(metadata=metadata)


class SessionStorage(Base):

    __tablename__ = "sessionstorage"
    uid = Column(Integer, primary_key=True)
    session_id = Column(String(36))
    service_name = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, session_id, service_name):
        self.session_id = session_id
        self.service_name = service_name
