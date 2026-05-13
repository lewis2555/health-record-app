"""
健康记录 APP - 用药和血压血糖记录
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from datetime import datetime
import os
class MainScreen(Screen):
    """主屏幕 - 显示功能菜单"""
    pass
class MedicationScreen(Screen):
    """用药记录屏幕"""
    def record_medication(self):
        """记录当前时间的用药"""
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M")
        # 这里可以添加保存到文件的逻辑
        print(f"💊 用药记录：{time_str}")
        self.manager.current.ids['status_label'].text = f"已记录：{time_str} 用药"
class BloodPressureScreen(Screen):
    """血压记录屏幕"""
    systolic_input = ObjectProperty(None)
    diastolic_input = ObjectProperty(None)
    
    def record_blood_pressure(self):
        """记录血压数据"""
        if self.systolic_input and self.diastolic_input:
            try:
                sys_val = self.systolic_input.text
                dia_val = self.diastolic_input.text
                now = datetime.now()
                time_str = now.strftime("%Y-%m-%d %H:%M")
                print(f"❤️ 血压记录：{time_str} - {sys_val}/{dia_val}")
                self.manager.current.ids['status_label'].text = f"已记录：{time_str} 血压 {sys_val}/{dia_val}"
            except Exception as e:
                print(f"错误：{e}")
class BloodSugarScreen(Screen):
    """血糖记录屏幕"""
    sugar_input = ObjectProperty(None)
    
    def record_blood_sugar(self):
        """记录血糖数据"""
        if self.sugar_input:
            try:
                sugar_val = self.sugar_input.text
                now = datetime.now()
                time_str = now.strftime("%Y-%m-%d %H:%M")
                print(f"🩸 血糖记录：{time_str} - {sugar_val}")
                self.manager.current.ids['status_label'].text = f"已记录：{time_str} 血糖 {sugar_val}"
            except Exception as e:
                print(f"错误：{e}")
class HealthApp(App):
    def build(self):
        self.title = "健康记录助手"
        return MainScreen()
if __name__ == '__main__':
    HealthApp().run()
