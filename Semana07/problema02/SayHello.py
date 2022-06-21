from cgitb import text
from tkinter import font
from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        '''Definições de widgets'''
        # Labels
        self.label = Label(text='Qual seu nome?', font_size = 18, color = '#FF24FF')

        # Entradas
        self.input = TextInput(multiline=False, padding_y = (20,20), size_hint = (1, 0.5))

        # Botões
        self.button = Button(text='Confirmar', size_hint = (1, 0.5), bold = True, background_color = '#FF24FF', 
                            background_normal = "")
        self.button.bind(on_press=self.callback)

        # Adicionando widgets

        self.window.add_widget(Image(source='images/marin.jpg'))
        self.window.add_widget(self.label)
        self.window.add_widget(self.input)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, intance):
        self.label.text = self.input.text

        

if __name__ == "__main__":
    SayHello().run()