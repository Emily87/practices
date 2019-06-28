对于telnet协议都是问答的字符串
port和timeout是可选的参数，而timeout的只是在初始化socket连接时起作用，而一旦连接成功后如果出现等待那就不会起作用了
dubbo接口说明：
接口地址：
http://ip:port/接口名
接口名
方法
参数
实例化Dubbo对象，传入host地址及port口
使用对象invoke方法吗，传入服务名称、方法名及传入json

ps:如果开发给配rpc或者hession,就可以用一些开源的库
需要在服务端配置这个：
Multi protocol:
 <dubbo:protocol name="dubbo" port="8080" />
 <dubbo:protocol name="jsonrpc" port="8080" />
 <dubbo:service id="Service" interface="cn.com.interface" version="1.0.0" protocol="dubbo,jsonrpc" />
 headers = {"Content-type": "application/json-rpc",
               "Accept": "text/json"}
    h1 = httplib.HTTPConnection('ip', port)
    h1.request("POST", '/com.qianmi.ofdc.api.phone.PhoneNoCheckProvider', json.dumps(app_params), headers)
    response = h1.getresponse()
    return response.read()
    就可以像用request像请求http接口一样；


