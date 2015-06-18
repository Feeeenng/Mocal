# -*- coding: utf8 -*-

class BaseController(object):
    def __init__(self, db_object):
        pass

    # get one
    def from_id(self, id):
        pass

    def from_db(self, **kwargs):
        pass

    # get more
    def fetch(self, **kwargs):
        pass

    # save
    def save(self):
        pass

    # get property
    def get_property(self, k):
        pass

    # set property
    def set_property(self, k, v):
        # TODO: check attr exist
        pass

    def set_properties(self, **kwargs):
        for k, v in kwargs.items():
            self.set_property(k, v)