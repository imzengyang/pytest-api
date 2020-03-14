import requests
from common.logger import Log

log = Log()


class SDKClient:
    @staticmethod
    def do_request(url:str, method:str, data:str,**kwargs):
        method = method.lower()
        log.info(f'开始请求- 请求路径: {url},请求方法: {method},请求参数: {data}, 其它参数: {kwargs}')
        try:
            if method == 'get':
                r = requests.get(url=url,params=data,**kwargs)
            elif method == 'post':
                r = requests.post(url=url,data=data,**kwargs)

            return r
        except Exception:
            log.error(f'发送请求时出错：错误详细信息 {Exception}')
