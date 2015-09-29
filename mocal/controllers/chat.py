# -*- coding: utf8 -*-

from base import BaseController, controller_with_dbobject
from models.chat import ChatMsgDBObject


@controller_with_dbobject(ChatMsgDBObject)
class ChatMsg(BaseController):
    def __init__(self, properties=None):
        super(ChatMsg, self).__init__(properties)