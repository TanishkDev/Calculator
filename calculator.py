from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from math import *
from kivy.core.window import Window

class CalcGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.funcs=[]

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self,keyboard,keycode,text,modifiers):
        print(keycode[1])
        if keycode[1]=="enter":
            self.evaluate()

    def on_click(self, button):
        expression = self.ids.input.text
        if "Error" in expression:
            expression = ""
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"


    def on_clear(self): 
        self.ids.input.text = ""

    def evaluate(self):
        expression = self.ids.input.text
        try:
            self.ids.input.text = str(eval(expression))
        except Exception as e:
            self.ids.input.text = "Error"


class Calculator(App):
    pass


Calculator().run()



