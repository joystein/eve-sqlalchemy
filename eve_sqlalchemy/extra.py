# -*- coding:utf-8 -*-

import hashlib

from eve import Eve

from sqlalchemy import func

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer
)

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

def get_etag():
    return hashlib.sha1().hexdigest()

class EveSqlalchemy(Eve):
    """
    EveSqlalchemy

    Code that is typically common for eve-sqlalchemy APIs and/or code that should be upstreamed to
    eve.
    """
    def __init__(self, auth, **kwargs):
        """
        We want that the auth object should have access to eve, just like objects of `media` and
        `data` keywords.
        """
        super(EveSqlalchemy, self).__init__(auth=auth(self), **kwargs)


class EveSqlalchemyBase(Base):
    """
    EveSqlalchemyBase
    """
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40), default=get_etag())
    id = Column(Integer, primary_key=True, autoincrement=True)
