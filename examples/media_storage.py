# -*- coding:utf-8 -*-

"""
 
 SQLBlobMediaStorage
 
 Example client command:
 
     $ curl -F "name=some_file.py" -F "content=@examples/media_storage.py" 127.0.0.1:5000/file
 
"""

import copy

from sqlalchemy import (
    Column,
    String,
    Integer,
    LargeBinary,
)

from sqlalchemy.orm import column_property

from eve import Eve
from eve.utils import config

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from eve_sqlalchemy.media import SQLBlobMediaStorage

from eve_sqlalchemy.extra import Base
from eve_sqlalchemy.extra import EveSqlalchemyBase

from eve_sqlalchemy.decorators import registerSchema


class FileMedia(EveSqlalchemyBase):
    __tablename__ = 'file_media'
    name = Column(String(80))
    content = Column(LargeBinary())


config.ID_FIELD = 'id'
config.ITEM_LOOKUP_FIELD = 'id'


registerSchema('file')(FileMedia)

file = copy.deepcopy(FileMedia._eve_schema['file'])

SETTINGS = {
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'RESOURCE_METHODS':['GET', 'POST'],
    
    'ID_FIELD':'id',
    'ITEM_LOOKUP_FIELD':'id',
    
    'DOMAIN': {
        'file': file,
        }
}


app = Eve(
    auth=None,
    settings=SETTINGS,
    validator=ValidatorSQL,
    data=SQL,
    media=SQLBlobMediaStorage
)

# bind SQLAlchemy
db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

app.run(debug=True, use_reloader=False)
