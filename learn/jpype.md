1.用idea给项目打个jar包 参考：https://blog.csdn.net/njxiaoxiao79/article/details/85679992
菜单栏File-->Project Structure打开Project Structure
点+按钮，选择JAR--》From Modules.....打开create jar from modules
Main Class 选择你要的类（否则最后打出的jar包缺少main-class属性导致无法执行）
然后修改MANIFEST.MF的存放路径 ，默认是..../src/... 务必改为 .../src
点OK进入下一步，如果弹出如下的错误提示，那是因为之前曾经打过jar，生成了MANIFEST.MF文件，删除这个文件就可以了
点菜单栏build-->build Artfacts...弹出对话框，选中刚刚生成的jar，会再弹出个对话框点击build
2.将jar包放到python项目下
 启动JVM
 加载jar包
 指定main class  （META-INF里的类名）
 创建类实例对象
 引用jar包类中的方法
 关闭JVM
 执行结果有个警告，一大串 不太懂 如果不想看那一大串警告可以改下源码
 _cour.py文件
     if not "convertStrings" in kwargs:
        import warnings
#        warnings.warn("""
-------------------------------------------------------------------------------
#Deprecated: convertStrings was not specified when starting the JVM. The default
#behavior in JPype will be False starting in JPype 0.8. The recommended setting
#for new code is convertStrings=False.  The legacy value of True was assumed for
#this session. If you are a user of an application that reported this warning,
#please file a ticket with the developer.
#-------------------------------------------------------------------------------
#""")
        warnings.warn('')