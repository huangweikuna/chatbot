import json

from django.http import JsonResponse
from rest_framework.views import APIView

from chat.core.rule_manager import manage
from chat.service.event_service import handler
from common import result
from common.lark_tools import AESCipher

EVENT_KEY = "ZA_DEVOPS"
aesc = AESCipher(EVENT_KEY)


class EventListenerView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if 'challenge' in data:
                return JsonResponse({
                    "CHALLENGE": aesc.decrypt_string(data['encrypt'])['challenge']
                })
            handler(data)
        except Exception as e:
            pass
        # always return ok
        return result.ok("ok")

