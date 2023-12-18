from appium.options.common.base import AppiumOptions
OPTIONS = AppiumOptions().load_capabilities({
    "platformName": "Android",
    "appium:automationName": "uiautomator2",
    "appium:platformVersion": "7.0",
    "appium:udid": "127.0.0.1:62025",
    "appium:appPackage": "com.nerversoft.ark.recode",
    "appium:appActivity": "com.unity3d.player.UnityPlayerActivity",
    "appium:noReset": True,
    "appium:newCommandTimeout": 3600,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
})
APPIUM_SERVER = "http://127.0.0.1:4723"