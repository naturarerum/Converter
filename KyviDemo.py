# This is a sample Python script.

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

kivy.require('2.0.1')
class MyWidget(Widget):
    pass

class KyviDemo(App):
    def build(self):
        return MyWidget()

if __name__ ==  '__main__':
    KyviDemo().run()



