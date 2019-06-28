import socket
import telnetlib
from pprint import pprint
import json


class DubboClient(telnetlib.Telnet):

    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        command_str = "invoke {0}.{1}({2})".format(
            service_name, method_name, json.dumps(arg))
        self.command(DubboClient.prompt, command_str)
        data = self.command(DubboClient.prompt, "")
        print(data)
        data = data.decode(DubboClient.coding,errors='ignore').split('\n')[0].strip()
        return data

    def do(self, arg):
        command_str = arg
        self.command(DubboClient.prompt, command_str)
        data = self.command(DubboClient.prompt, command_str)
        data = data.decode(DubboClient.coding,errors='ignore').split('\n')[0].strip()
        return data

if __name__ == '__main__':

    conn = DubboClient('10.27.14.141', 20880)
    res = conn.invoke('cn.com.autohome.openPlatform.api.ProviderAPI', 'queryProviderlistForRedPack', {
        "provinceId": 110000,
        "cityId  ": 110100,
    })
    print(json.loads(res))
    arg = {
        "provinceId": 110000,
        "cityId  ": 110100,
    }
    command_str = 'invoke cn.com.api.ProviderAPI.queryProviderlist(arg)'
    print(conn.do(command_str))
    print(len(json.loads(res)['result']))

    # service_name = 'cn.com.autohome.openPlatform.api.ProviderAPI'
    # method_name = 'queryProviderlistForRedPack'
    # arg = {
    #     "provinceId": 110000,
    #     "cityId  ": 110100,
    # }
    # command_str = "invoke {0}.{1}({2})".format(
    #     service_name, method_name, json.dumps(arg))
    # r = conn.command(DubboClient.prompt, command_str)
    # print(r)
    # d = conn.invoke(service_name,method_name,arg)
    # print(d)

    # e = conn.do(command_str)
    # print(e)
    # print(len(json.loads(e)['result']))
