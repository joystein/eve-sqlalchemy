# -*- coding:utf-8 -*-

"""
 
 SQLBlobMediaStorage
 
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy import (
    Column,
    String,
    Integer,
    LargeBinary,
)

from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

# Eve-SQLAlchemy imports
from eve_sqlalchemy.decorators import registerSchema

Base = declarative_base()


class FileMedia(Base):
    __tablename__ = 'file_media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    file = Column(LargeBinary())


registerSchema('file_media')(FileMedia)

SETTINGS = {
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'DOMAIN': {
        'file': FileMedia._eve_schema['file_media'],
        }
}

app = Eve(auth=None, settings=SETTINGS, validator=ValidatorSQL, data=SQL)

app.run(debug=True, use_reloader=False)
