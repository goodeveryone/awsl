import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
init_device("Android")
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 点击返回键
# keyevent("BACK")

# 点击浏览器
# poco("com.mumu.launcher:id/workspace").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")[2].click()
# poco("com.miui.home:id/workspace").offspring("天气").offspring("com.miui.home:id/icon_icon").click()

# # 屏幕左滑
# swipe((200,1300),(900,1300))
# time.sleep(2)
# # 屏幕右滑
# swipe((900,1300),(200,1300))
# time.sleep(2)
# # 点击LAJI文件夹
# touch((666,505))
# time.sleep(1)
# # 点击摇钱车app
# touch((271,978))
# time.sleep(3)
# # 点击广告按钮
# touch((328,2239))
# time.sleep(1)
# # 点击往期广告按钮
# touch((901,296))
# time.sleep(5)
# # 点击查看详情按钮
# touch(928,853)
# time.sleep(1)
# # 屏幕上滑
# swipe((567,1938),(567,653))
# time.sleep(3)
# # 点击“HOME”键回到主页面
# for i in range(2):
#     keyevent("HOME")
#     time.sleep(1)
# 点击“看”文件夹
touch((928,215))
# 点击哔哩哔哩app
time.sleep(1)
touch((818,822))
# 点击跳过
touch(900,544)
time.sleep(5)
# 点击追番
touch(599,285)
time.sleep(1)
# 点击我的追番第一项
touch(184,1347)
time.sleep(1)
