# -*- coding:utf-8 -*-

from eve import Eve


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
