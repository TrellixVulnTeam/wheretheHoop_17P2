from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
#to create a text input box
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
#from line 5 of FFA main.py
# BoxLayout arranges widgets in either 
# in vertical fashion that 
# is one on top of another or in 
# horizontal fashion that is one after another. 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
class MyGrid(Widget):
    userId = ObjectProperty(None)
    zipC = ObjectProperty(None)

    def btn(self):
        print("userId:", self.userId.text, "zipC:", self.zipC.text)
        self.userId.text = ""
        self.zipC.text = ""




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()