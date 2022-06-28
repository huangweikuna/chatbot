import json
import time

from chat.core.rule_manager import manage

CHECK_PARAM = ['schema', 'header', 'event']

"""
 {
    "schema": "2.0", // 事件格式的版本。无此字段的即为1.0
    "header": {
        "event_id": "f7984f25108f8137722bb63cee927e66",  // 事件的唯一标识
        "token": "066zT6pS4QCbgj5Do145GfDbbagCHGgF", // 即Verification Token
        "create_time": "1603977298000000", //  事件发送的时间
        "event_type": "contact.user_group.created_v3", // 事件类型
        "tenant_key": "xxxxxxx",  // 企业标识
        "app_id": "cli_xxxxxxxx", // 应用ID
    },
    "event":{
        {
            "message": {
                "chat_id": "oc_1259854f99ad326ee717089ba94f3b2d", 
                "chat_type": "p2p", "content": "{\"text\":\"test\"}",
                "create_time": "1656387578471", 
                "message_id": "",
                "message_type": "text"
            }, 
            "sender": {
                "sender_id": {
                    "open_id": "", 
                    "union_id": "",
                    "user_id": ""
                }, 
                "sender_type": "user", 
                "tenant_key": "12f8473c5b4f5759"}
            }
    }
}
"""


def handler(event):
    for p in CHECK_PARAM:
        if p not in event:
            # TODO log
            return
    if event['header']['create_time'] < int(round(time.time() * 1000)) - 1 * 60 * 1000:
        return
    manage.call(json.loads(event['event']['message']['content'])['text'])
