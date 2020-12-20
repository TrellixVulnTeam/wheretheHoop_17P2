from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
#to create a text input box
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
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


#create Screen class for kivy to add new screen to program

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass



class MainApp(App):
    def build(self):
        return
    	# #fix button size, position button near box, fix box size
    	# button click function
    	# def buttonClicked(self,btn):
    	# 	self.lbl1.text = "You wrote " + self.txt1.text
    	
    	

    	# b = BoxLayout(orientation ='vertical')
    	# label = Label(text='Please enter your zipcode',
     #                  size_hint=(.5, .5),
     #                  pos_hint={'center_x': .5, 'center_y': .5})
    	# textInput = TextInput(text = '', multiline= False)
    	# b.add_widget(textInput)
    	# return label

if __name__ == '__main__':
    app = MainApp()
    app.run()