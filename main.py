from tkinter import N
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#size of screen
Window.size = (320,650)
Builder.load_file('design.kv')  #loading kivy file

#importing widget from kivy file
class MyLayout(Widget):
    def allClear(self):
        self.ids.calc_input.text= "0"
    def Clear(self):
        previous = self.ids.calc_input.text
        previous = previous[:-1]
        self.ids.calc_input.text = previous

    def PosNegconvert(self):
        previous = self.ids.calc_input.text
        if "-" in previous:
            self.ids.calc_input.text= f'{previous.replace("-","")}'
        else:    
            self.ids.calc_input.text= f'-{previous}'
        
      # fun() for numbers  
    def num_press(self, btn):
        previous = self.ids.calc_input.text
        if "ERROR" in previous:
            previous=''
        if previous == "0":
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{btn}'
        else:
            self.ids.calc_input.text = f'{previous}{btn}'  
        self.ids.calc_input.text
        
    def Add(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}+'
    def Sub(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}-'
    def Multiply(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}*'
    def Division(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}/'
    def Reminder(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}%'
    def Power(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}**'
    def P_root(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}**0.5'
    def Pie(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous}*3.14'
    def BracketOp(self):
        previous = self.ids.calc_input.text
        if "(" in previous:
            self.ids.calc_input.text= f'{previous}('
        else:    
            self.ids.calc_input.text= f'({previous}'
    def BracketCls(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text= f'{previous})'
    def Period(self):
        previous = self.ids.calc_input.text
        num_list = previous.split("+")
        if "+" in previous and "." not in num_list[-1]:
            previous=f'{previous}.'
            self.ids.calc_input.text = previous
        elif "." in previous:
            pass
        else:
            previous=f'{previous}.'
            self.ids.calc_input.text = previous
        
                
    
    def Solution(self):
        previous = self.ids.calc_input.text 
        try:
            answer = eval(previous)
            self.ids.calc_input.text= str(answer)
        except:  
            self.ids.calc_input.text= "ERROR"
            
            
        

#App initialization
class CalciApp(App):
    def build(self):
        return MyLayout()

#Appcall
if __name__ == '__main__':
    CalciApp().run()
