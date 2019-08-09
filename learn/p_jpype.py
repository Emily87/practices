import jpype

# jvmPath = jpype.getDefaultJVMPath()
# print(jvmPath)
def get_sign(sign):
    """
    调用java jar包，对入参进行rsa签名
    :param sign_raw:待签名字符串
    :return:signature:签名后的加密字符串
    """
    # 启动JVM
    jvmPath = jpype.getDefaultJVMPath()
    # 加载jar包
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=demo.jar")
    # 指定main class
    JDClass = jpype.JClass("ProviderInfoInterface")
    # 创建类实例对象
    jd = JDClass()
    # 引用jar包类中的方法 rsa_sign
    signature = jd.encryptionOfLower(sign)
    # signature = jd.rsa_sign(sign_raw)
    # 关闭JVM
    jpype.shutdownJVM()
    return signature

if __name__ == '__main__':
    print(get_sign('aaa'))

