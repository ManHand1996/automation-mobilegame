from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions import images_comparison

import time
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import base64
from ark_recode.main import ARKRecode

"""
windows 下 npm全局安装位置
npm -g install xx
%userprofile%\\AppData\Roaming\\npm\\node_modules
C:\\Users\\86134\\AppData\\Roaming\\npm\\node_modules

APPIUM_HOME默认：
使用appium driver|plugin install xx 会安装在： 
%userprofile%\\.appium
C:\\Users\86134\\.appium
"""
ARKRecode().run()

# options = AppiumOptions()
# options.load_capabilities({
#     "platformName": "Android",
#     "appium:automationName": "uiautomator2",
#     "appium:platformVersion": "7.0",
#     "appium:udid": "127.0.0.1:62025",
#     # "appium:appPackage": "com.nerversoft.ark.recode",
#     # "appium:appActivity": "com.unity3d.player.UnityPlayerActivity",
#     "appium:noReset": True,
#     "appium:ensureWebviewsHavePages": True,
#     "appium:nativeWebScreenshot": True,
# })

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# 启动游戏界面： '点击进入游戏'
# with open('images\\lunch-game.png', 'rb') as lunch:
#     lunch_img = base64.urlsafe_b64encode(lunch.read()).decode('ascii')
# while True:
#     cur_screen = driver.get_screenshot_as_base64()
#     try:
#         # 匹配成功后
#         res = driver.find_image_occurrence(cur_screen, lunch_img, threshold=0.8, visualize=True)
#         el = driver.find_element(by=AppiumBy.IMAGE, value=res['visualization'])
#         el.click()
#         print(res)
#     except:
#         time.sleep(1)
#     else:
#         break


# 游戏界面：公告弹出
# with open('images\\close-announcement.png', 'rb') as lunch:
#     announce_img = base64.urlsafe_b64encode(lunch.read()).decode('ascii')
# while True:
#     cur_screen = driver.get_screenshot_as_base64()
#     try:
#         # 匹配成功后
#         res = driver.find_image_occurrence(cur_screen, announce_img, threshold=0.8, visualize=True)
#         actions = ActionChains(driver)
#         actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#         actions.w3c_actions.pointer_action.move_to_location(res['rect']['x'], res['rect']['y'])
#         actions.w3c_actions.pointer_action.pointer_down()
#         actions.w3c_actions.pointer_action.pause(0.1)
#         actions.w3c_actions.pointer_action.release()
#         actions.perform()
#         time.sleep(1)
#         print(res)
#     except:
#         time.sleep(1)
#     else:
#         break


# with open('images\\index.png', 'rb') as img1:
#     b64_img1 = base64.urlsafe_b64encode(img1.read()).decode('ascii')

# with open('images\\start.png', 'rb') as img2:
#     # TypeError: Object of type bytes is not JSON serializable
#     b64_img2 = base64.urlsafe_b64encode(img2.read()).decode('ascii')
# print(b64_img1)

# # {'rect': {'x': 1196, 'y': 465, 'width': 198, 'height': 248}, 'score': 0.42227375507354736, 'visualization': None, 
# #  'multiple': [{'score': 0.42227375507354736, 'rect': {'x': 1196, 'y': 465, 'width': 198, 'height': 248}}]}
# print(res)
# time.sleep(10)
# driver.quit()

