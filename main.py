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


#create Screen class for kivy to add new screen to program

class HomeScreen(Screen):
	pass

#GUI
class MainApp(App):
    def build(self):
    	layout = BoxLayout(padding=10, orientation='vertical')
    	btn1 = Button(text="Enter", size_hint = (.125, .125))
    	#btn1.bind(on_press=self.buttonClicked)
    	layout.add_widget(btn1)
    	self.lbl1 = Label(text="Please enter your zipcode", size_hint = (.5, .5))
    	layout.add_widget(self.lbl1)
    	self.txtbox1 = TextInput(text='', multiline=False)
    	layout.add_widget(self.txtbox1)
    	return layout
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