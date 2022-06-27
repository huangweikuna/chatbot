import logging
import traceback

from django.http import JsonResponse

logger = logging.getLogger(__name__)


# 自定义状态码
class HttpCode(object):
    # 正常登陆
    ok = 0
    # 参数错误
    paramserror = 400
    # 权限错误
    unauth = 401
    # 方法错误
    methoderror = 405
    # 服务器内部错误
    servererror = 500


# 定义统一的 json 字符串返回格式
def result(code=HttpCode.ok, message="", data=None, kwargs=None):
    json_dict = {"code": code, "message": message, "data": data}
    # isinstance(object对象, 类型):判断是否数据xx类型
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


def ok(data=None):
    return result(message="success", data=data)


# 参数错误
def params_error(message="", data=None, ex=None):
    log_ex(ex)
    return result(code=HttpCode.paramserror, message="[params_error] : " + message, data=data)


# 权限错误
def unauth(message="", data=None, ex=None):
    log_ex(ex)
    return result(code=HttpCode.unauth, message="[unauth] : " + message, data=data)


# 方法错误
def method_error(message="", data=None, ex=None):
    log_ex(ex)
    return result(code=HttpCode.methoderror, message="[method_error] : " + message, data=data)


# 服务器内部错误
def server_error(message="", data=None, ex=None):
    log_ex(ex)
    return result(code=HttpCode.servererror, message="[server_error] : " + message, data=data)


def log_ex(ex):
    if ex:
        logger.error(str(ex))
        logger.error(traceback.format_exc())
