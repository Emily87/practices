from arrow import utcnow
from hashlib import md5
import requests


def get_sign_params(params: dict, appkey):
    params.setdefault('_timestamp', utcnow().timestamp)
    sign = ''
    for i in sorted(params.items(), key=lambda x: x[0]):
        sign += ''.join([str(j) for j in i])
    new_md5 = md5()
    new_md5.update((appkey+sign+appkey).encode())
    _sign = new_md5.hexdigest().upper()
    return _sign
    # params.setdefault('_sign', new_md5.hexdigest().upper())
    # return params

def ProviderInfoInterface(params):
    params.setdefault('_sign', get_sign_params(param,appkey))
    return params



if __name__ == '__main__':
    param = {'providerId': xxx, 'platformType': x, '_appid': "xxxx"}
    appkey = "xxx"
    url = "xxx"
    # print(requests.get(url, params=get_sign_params(param, appkey)).json())
    # print(requests.post(url, data=get_sign_params(param, appkey)).json())
    #print(get_sign_params(param,appkey))
    print(ProviderInfoInterface(param))
    print(requests.post(url, data=ProviderInfoInterface(param)).json())

