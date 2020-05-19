# python_android_frame
appium android frame for xueqiu demo

安装说明
一、工具环境
a.  系统： windows环境(demo为win7)
b. jdk 1.8
c. android sdk (主要用uiautomatorviewer，adb)(链接: https://pan.baidu.com/s/1DhZ2m3Yb5Sb06SwDZ-

6khw 提取码: v1gp) 
d. appium server 1.8 (安装appium-desktop1.8，包含server和inspect：与uiautomator功能类似)（链接: 

https://pan.baidu.com/s/1ALgxVQkKcOSn6DR9uuDACw 提取码: yvuq）
e. Node.js 版本 10。（链接: https://pan.baidu.com/s/1ALgxVQkKcOSn6DR9uuDACw 提取码: yvuq ）
f. phone模拟器MoMo
g. pip install Appium-Python-Client Selenium


二、启动
a. 启动appium server
b. 启动模拟器（安装好要测试的apk）
c. 连接模拟器 adb connect 127.0.0.1:7555
d. 查看app包名和activity ：  adb logcat| grep -i displayed
e. 编码调用server发起请求


三、遇到过的问题记录
1. mumu模拟器无menu键如何杀掉进程？
       任务栏设置-》清理内存， 实际是重启android
       or 点top区sheet标签关闭

2. uiautomatorview 获取的屏幕是横的？
   原因：模拟器默认为横屏，只是打开应用时显示为竖屏，uiautomatorviewer识别时，根据分辨率，将app识别为

横屏
  解决：a:进入设置中心–>界面设置–>分辨率设置–>自定义
           b:修改分辨率为竖屏，eg:宽：720，高：1280
   
 3 . uiautomatorviewer识别不到模拟器
    报 Error while obtaining UI hierarchy XML file: com.android.ddmlib.SyncException
    解决： 关闭再启动appium服务

4、python 脚本执行时报错
 log：url: /wd/hub/session (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object 

at 0x0000000004F836A0>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，

无法连接。'))
  解决：appium服务无法识别导致， 重启server
