import sys
import time
import base64
import logging
logging.basicConfig(level=logging.INFO)

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# 导入问题：
# 如果在当前module下使用 __name__ == '__main__' 运行
# 当前解释器就会从当前路径开始搜索module
# 如果包含当前module的文件夹下有__init__.py(package) 则如果想使用 from packgename.module_name import func
# 会报错， 使用相对路径导入也会报错 from .module_name import func
from config import OPTIONS, APPIUM_SERVER

class ARKRecode:
    
    ele_types = {
        'dark': 'dark_element.png',
        'fire': 'fire_element.png',
        'ocean': 'ocean_element.png',
        'wood': 'wood_element.png',
        'light': 'light_element.png',
    }
    ele_level = {
        0: 'level_0.png',
        1: 'level_1.png',
        2: 'level_2.png',
        3: 'level_3.png',
    }
    
    def __init__(self) -> None:
        """
        init driver
        """
        
        self.driver = webdriver.Remote(APPIUM_SERVER, options=OPTIONS)
    
    def _match_image(self, image_path, click=True, try_times=5, x=0, y=0, threshold=0.8, wait=0.3):
        """
        图片匹配最多尝试try_times后停止

        Args:
            image_path (string): image absolute path
            click (bool, optional): 匹配成功后是否点击
            try_times (int, optional): 重试次数. Defaults to 5. if try_times < 0:unlimit
            x (int, optional): 点击x位置, 默认=0,则选择匹配图片的rect.x
            y (int, optional): 点击y位置, 默认=0,则选择匹配图片的rect.y
            threshold (float, optional): 匹配阈值. Defaults to 0.8. 
            wait （float, optional): 每次匹配等待时间. Defaults to 0.3
            
        Returns: True if found image else False
        """
        res = None
        with open(image_path, 'rb') as img:
            target = base64.b64encode(img.read()).decode('ascii')
        while True:
            cur_screen = self.driver.get_screenshot_as_base64()
            logging.info(f'{image_path}, wati {wait} secs')
            try:
                # 匹配成功后
                try_times -= 1
                res = self.driver.find_image_occurrence(cur_screen, target, threshold=threshold, visualize=True)
                print(f'res:{res}')
                x = x if x else res['rect']['x']
                y = y if y else res['rect']['y']
                if click:
                    self._click_byPos(x, y)
                
                
            except:
                if try_times == 0:
                    break
                else:
                    time.sleep(wait)
            else:
                break
        return False if not res else res
    
    
    def _scroll_byPos(self, x, y, to_x, to_y, pause=0.1):
        """从(x,y)滑动到(to_x, to_y)

        Args:
            x (_type_): start x
            y (_type_): start y
            to_x (_type_): end x
            to_y (_type_): end y
            pause (float, optional): 点击停留时间(越短滑动得越多越快). Defaults to 0.1.
        """
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(pause)
        actions.w3c_actions.pointer_action.move_to_location(to_x, to_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    
    
    def boot(self):
        """
        启动游戏界面： '点击进入游戏'
        """
        self._match_image('images\\lunch_game.png')
        
            
    def _click_byPos(self, x, y):
        """
        点击图片

        Args:
            x (_type_): 图片左上角横坐标
            y (_type_): 图片左上角纵坐标
        """
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
        
    def announcement(self):
        """
        公告弹出
        """
        # 游戏界面：公告弹出
        self._match_image('images\\close_announcement.png')
           
    
    def new_character(self):
        """
        新角色弹出介绍
        """
        # 捕获异常后，再判断是否已进入index.png 这个界面（有无这个界面下特别的元素：'出击'）
        self._match_image('images\\new_char_confirm.png')
        
    
    def mission_deliver(self):
        """
        任务派遣
        """
        self._match_image('images\\mission_deliver.png', x=1482, y=855)
        self._match_image('images\\mission_deliver.png', x=1482, y=855)
        

    
    def month_arrived(self):
        """
        每日签到界面
        """
        self._match_image('images\\month_arrived.png', x=1899, y=139)
        
        
    def support(self):
        """
        辅助团员友情点数界面
        """
        self._match_image('images\\support.png', x=1899, y=139)

    
    def hit_out(self):
        """
        主页面：出击
        """
        self._click_byPos(0,0)
        self._match_image('images\\hit_out.png', x=2155, y=806)

    
    def elements_explore(self, ele_type='dark', repeat=1, level=0):
        """
        战斗-元素探索

        Args:
            ele_type (str, optional): 元素类型. Defaults to 'dark'.
            repeat (int, optional): 重复战斗次数. Defaults to 1.
        """
        self.ele_types[ele_type]
        self.ele_level[level]
        self._match_image('images\\element_explore\\index.png')
        if ele_type in ('wood', 'light'):
            time.sleep(0.5)
            self._scroll_byPos(1600, 940, 1600, 130)
        self._match_image(f'images\\element_explore\\{self.ele_types[ele_type]}')
        self._match_image(f'images\\element_explore\\{self.ele_level[level]}')
        self._match_image(f'images\\team_setting.png', x=2078, y=965)
        self.repeat_setting(repeat)
        self.back_toFightIndex()


    def event_story(self, repeat=3, level='A1'):
        """战斗-活动故事
        """
        # 进入活动
        self._click_byPos(x=600, y=500)
        self._match_image('images\\event_story\\story_start.png', threshold=0.9)
        level_img = f'story_{level}.png'
        # 滑动到对应level
        level_res = self._match_image(f'images\\event_story\\{level_img}', threshold=0.9)
        while not level_res:
            self._scroll_byPos(x=1850, y=750, to_x=900, to_y=750, pause=1)
            level_res = self._match_image(f'images\\event_story\\{level_img}',  threshold=0.9, wait=1)
        
        if level != 'A1':
            self._match_image('images\\event_story\\team_setting.png', x=2078, y=965)
        
        # self._match_image('images\\fight.png')
        self.repeat_setting(repeat)
        self.back_toFightIndex()
    
    
    def repeat_setting(self, repeat=3):
        """
        重复战斗设置
        每次自动战斗(系统)进行5小次
        共进行repeat * 5 次
        Args:
            repeat (int, optional): 重新进行n次. Defaults to 3.
        """
        if not self._match_image('images\\repeat_settings\\repeat_max.png', click=False):
            self._match_image('images\\repeat_settings\\repeat_setting.png')
            self._match_image('images\\repeat_settings\\repeat_setting_max.png')
            self._click_byPos(0,0) # 取消重复战斗设置界面
        self._match_image('images\\repeat_settings\\repeat_check.png', try_times=2, threshold=0.9)
        # if res:
        #     with open('images\\vis.png', 'wb') as img:
                
        #         img.write(base64.b64decode(res['visualization']))
        self._match_image('images\\fight.png')
        
        # wait firt repeat after 35 times try
        res = self._match_image('images\\repeat_settings\\repeat_again.png', click=False,
                                try_times=35, threshold=0.9 ,wait=10)
        
        while repeat-1:
            # 进行5次战斗
            res = self._match_image('images\\repeat_settings\\repeat_again.png',  try_times=35, threshold=0.9 ,wait=10)
            if res:
                repeat -=1
            else:
                print('5分钟内没有完成5次战斗... 5秒后重试')
                time.sleep(5)
        # 重复战斗结束
        print('start find repeat')
        res = self._match_image('images\\repeat_settings\\repeat_end.png', click=False, try_times=100, threshold=0.95, wait=10)
        if res:
            self._match_image('images\\fight_end_confirm.png', try_times=5, threshold=0.99, wait=0.3)
            print('已完成重复战斗...')
        
    
    def back_toFightIndex(self):
        """返回出击后的界面
        
        """
        self._match_image('images\\back.png', threshold=0.9)
        self._match_image('images\\back.png', threshold=0.9)
    
    def run(self):
        # self.boot()
        # self.announcement()
        # self.mission_deliver()
        # self.month_arrived()
        # self.support()
        # self.hit_out()
        # self.elements_explore(ele_type='ocean', level=2)
        # self.back_toFightIndex()
        # self.event_story()
        # self._match_image('images\\event_story\\story_hard2.png', threshold=0.85)
        
        self.event_story(level='hard')
        print('quit driver...')
        self.driver.quit()
        
if __name__ == '__main__':
    ARKRecode().run()