# How to import widgets
# all types of elements,widgets,layout import from kivy.uix.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


# we must define two types of size constrain
class BoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")
        button1 = Button(text='button 1', size_hint=(None,None),size=(200,50))
        button2 = Button(text='button 2', size_hint=(None,None),size=(200,50))

        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout
# BoxLayoutExample().run()



from kivy.uix.gridlayout import GridLayout

class GridLayoutExample(App):
    def build(self):
        layout = GridLayout(cols=4)
        for i in range(1,10):
              button = Button(text=f"Button {i}", size_hint=(None,None), size=(200,50))
              layout.add_widget(button)
        return layout
# GridLayoutExample().run()




from kivy.uix.floatlayout import FloatLayout

class FloatLayoutExample(App):
    def build(self):
        layout = FloatLayout()
        button1 = Button(text='button 1', size_hint=(None,None),size=(200,50),pos=(150,200))
        button2 = Button(text='button 2', size_hint=(None,None),size=(200,50),pos=(350,100))

        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout
# FloatLayoutExample().run()





from kivy.uix.relativelayout import RelativeLayout

class RelativeLayoutExample(App):
    def build(self):
        layout = RelativeLayout()
        button1 = Button(text='button 1', size_hint=(None,None),size=(200,50),pos_hint={'x':.6,'y':.5})
        button2 = Button(text='button 2', size_hint=(None,None),size=(200,50),pos_hint={'x': 0,'y': 0})

        button2.pos_hint = ({'x' : button1.pos_hint['x']+.1, 'y' : button1.pos_hint['y']-.1})

        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout
# RelativeLayoutExample().run()




from kivy.uix.stacklayout import StackLayout
#  position top to bottom and left to right (orientation='tb-lr')
#  position left to right and top to bottom (orientation='lr-tb')
class StackLayoutExample(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb')
        for  i in range(1,41):
            button = Button(text=f'Button {i}',size_hint=(None,None),size=(200,50))
            layout.add_widget(button)
        return layout
# StackLayoutExample().run()




from kivy.uix.anchorlayout import AnchorLayout
#  anchor_x(left,center,right)   anchor_y(top,center,bottom)
class AnchorLayoutExample(App):
    def build(self):
        layout = AnchorLayout(anchor_x='left',anchor_y='center')
        button = Button(text= 'Button',size_hint=(.2,.1))
        layout.add_widget(button)
        return layout
AnchorLayoutExample().run()
