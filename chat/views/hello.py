import json

from rest_framework.views import APIView

from common import result
from chat.core.rule_manager import manage


class HelloView(APIView):
    def get(self, request):
        print([r.get_order() for r in manage.rules])
        manage.call(request.GET.get('msg', ""))
        return result.ok("ok")
