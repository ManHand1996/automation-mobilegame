from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy

import time
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

"""
windows 下 npm全局安装位置
npm -g install xx
%userprofile%\AppData\Roaming\npm\node_modules
C:\Users\86134\AppData\Roaming\npm\node_modules

APPIUM_HOME默认：
使用appium driver|plugin install xx 会安装在： 
%userprofile%\.appium
C:\Users\86134\.appium
"""



driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

driver.match_images_features
# 出击
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(2155, 806)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 元素探索
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1420, 751)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 火元素
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1705, 861)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 火元素-初级
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1738, 225)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 队伍设置
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(2078, 965)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)

# 重复战斗设置
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(2281, 833)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 重复战斗-最多
driver.switch_to.context('NATIVE_APP')
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1727, 773)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 空白处：退出重复战斗设置
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(2144, 943)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)
# 勾选重复战斗 如果已经勾选则不需要。
# 需要截图然后识别该图片
# 使用opencv, appium:plugin:images 进行图片比较：a截图(某个按钮的截图)是否在b截图(全屏截图)中
# Q1: 如果获取部分图片？


actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(2028, 817)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(1)

driver.get_screenshot_as_base64
# # 开始战斗
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(2165, 965)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()


# # 重新开始
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(1837, 1003)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()


driver.quit()