from server.models import UserInfo
import xml.etree.ElementTree as ET
import time
import datetime
import cmn
import os


def helper():
    pass


def router(con):
    option = str(con).strip().split()[0:3]
    op1 = option[0] if len(option) > 0 else ""
    op2 = option[1] if len(option) > 1 else ""
    op3 = option[2] if len(option) > 2 else ""
    



class WeChatApi:
    def __init__(self, data):
        self.xmlData = ET.fromstring(data)
        self.con = self.xmlData.find("Content").text
        self.req_time = self.xmlData.find("CreateTime").text
        self.msg_type = self.xmlData.find("MsgType").text
        self.from_user = self.xmlData.find("FromUserName").text
        self.con_dict = {
            "msg_id": self.xmlData.find("MsgId").text,
            "create_time": int(time.time()),
            "to_name": self.from_user,
            "from_name": self.xmlData.find("ToUserName").text
        }
        u = UserInfo.objects.filter(wechat=self.from_user).first()
        if u:
            self.user = u

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
    
    def get_msg(self):
        if self.msg.msg_type == "text":
            return self.get_text_msg()
        else:
            return self.get_text_msg("Error")

