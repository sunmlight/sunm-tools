import xml.etree.ElementTree as ET
import time
import datetime
import cmn
import os


class Msg:
    def __init__(self, data):
        self.xmlData = ET.fromstring(data)
        self.con = self.xmlData.find("Content").text
        self.req_time = self.xmlData.find("CreateTime").text
        self.msg_type = self.xmlData.find("MsgType").text
        self.from_user = self.xmlData.find("FromUserName").text
        self.con_dict = {}
        self.con_dict["msg_id"] = self.xmlData.find("MsgId").text
        self.con_dict["create_time"] = int(time.time())
        self.con_dict["to_name"] = self.from_user
        self.con_dict["from_name"] = self.xmlData.find("ToUserName").text

    def get_text_msg(self, content):
        self.con_dict["con"] = content
        _r = """
        <xml>
          <ToUserName><![CDATA[{to_name}]]></ToUserName>
          <FromUserName><![CDATA[{from_name}]]></FromUserName>
          <CreateTime>{create_time}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{con}]]></Content>
          <MsgId>{msg_id}</MsgId>
        </xml>
        """.format(
            **self.con_dict
        )
        return _r


def get_msg(xml):
    msg = Msg(xml)
    if msg.msg_type == "text":
        if msg.con == "time":
            return msg.get_text_msg(cmn.date_now())
        elif msg.con == "你好":
            return msg.get_text_msg("Hello")
        else:
            return msg.get_text_msg("%s" % msg.con)
    else:
        return msg.get_text_msg("~")
