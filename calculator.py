from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from math import *
from kivy.core.window import Window
from kivy.properties import DictProperty

class CalcGridLayout(GridLayout):
    interesting=DictProperty()
    keys=DictProperty({
            '7':'/',
            '0':'=',
            "'":"*"
            })

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        # self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self,keyboard,keycode,text,modifiers):
        key=keycode[1]
        if key=="enter":
            self.evaluate()
        if key=="shift":
            self.interesting[key]='304'
        if key.isdigit() or key in self.keys:
            if 'shift' in self.interesting and key in self.keys:
                self.ids.input.text+=self.keys.get(key)
                del self.interesting['shift']
            else:
                self.ids.input.text+=key

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



