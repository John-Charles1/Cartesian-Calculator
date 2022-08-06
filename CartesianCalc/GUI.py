import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import calc

class gui:
    def __init__(self):
        layout = [  [sg.Text('Which Conic Section do you want to graph?')],
                    [sg.Button('Ellipse/Circle', key = "Ellipse/Circle")],
                    [sg.Button('Parabola', key = 'Parabola')],
                    [sg.Button('Hyperbola', key = 'Hyperbola')]
               ]
        window = sg.Window('Pick a conic', layout)
        self.main_loop(window)

    def main_loop(self, window):
        while True:                  # the event loop
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Ellipse/Circle':
                self.ellipse_window()
            if event == 'Parabola':
                self.parabola_window()
            if event == 'Hyperbola':
                self.hyperparabola_window()
        window.close()
    
    def ellipse_window(self):
        layout = [
            [sg.Text('(x-h)^2/a^2+(y-k)^2/b^2=1', size=(25,1), key = 'A')],
            [sg.Text('a', size=(8,1), key = 'A'), sg.Input()],
            [sg.Text('b', size=(8,1), key = 'B'), sg.Input()],
            [sg.Text('h', size=(8,1), key = 'H'), sg.Input()],
            [sg.Text('k', size=(8,1), key = 'K'), sg.Input()],
            [sg.Button('Graph', size=(8,1), key='graph')]
        ]
        window = sg.Window('asd', layout)
        while True:                  # the event loop
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'graph':
                try:
                    c = calc.conic()
                    c.ellipse_circle(float(values[0]), float(values[1]), int(values[2]), int(values[3]))
                    c.show()
                except:
                    sg.Popup('Decimal Numbers Only for a and b, whole numbers only for h and k')

    def parabola_window(self):
        layout = [
            [sg.Text('x^2 = 4ay', size=(25,1))],
            [sg.Radio('Open Up', "RADIO1", default=False, key="up")],
            [sg.Text('x^2 = 4(-a)y', size=(25,1))],
            [sg.Radio('Open Down', "RADIO1", default=True, key="down")],
            [sg.Text('y^2 = 4(-a)x', size=(25,1))],
            [sg.Radio('Open Left', "RADIO1", default=False, key="left")],
            [sg.Text('y^2 = 4ax', size=(25,1))],
            [sg.Radio('Open Right', "RADIO1", default=False, key="right")],
            [sg.Text('a', size=(8,1), key = 'A'), sg.Input()],
            [sg.Text('h', size=(8,1), key = 'H'), sg.Input()],
            [sg.Text('k', size=(8,1), key = 'K'), sg.Input()],
            [sg.Button('Graph', size=(8,1), key="graph")],
        ]
        window = sg.Window('asd', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if values["up"] == True:
                try:
                    c = calc.conic()
                    c.up_parabola(float(values[0]), float(values[1]), float(values[2]))
                    c.show()
                except:
                    sg.Popup("Decimal Number only for \'a\'")
            if values["down"] == True:
                try:
                    c = calc.conic()
                    c.down_parabola(float(values[0]), float(values[1]), float(values[2]))
                    c.show()
                except:
                    sg.Popup("Decimal Number only for \'a\'")
            if values["left"] == True:
                try:
                    c = calc.conic()
                    c.left_parabola(float(values[0]), float(values[1]), float(values[2]))
                    c.show()
                except:
                    sg.Popup("Decimal Number only for \'a\'")
            if values["right"] == True:
                try:
                    c = calc.conic()
                    c.right_parabola(float(values[0]), float(values[1]), float(values[2]))
                    c.show()
                except:
                    sg.Popup("Decimal Number only for \'a\'")

    def hyperparabola_window(self):
        layout = [
            [sg.Text('x^2/a^2 - y^2/b^2 = 1 where a,b > 0', size=(35,1))],
            [sg.Text('a', size=(8,1), key = 'A'), sg.Input()],
            [sg.Text('b', size=(8,1), key = 'B'), sg.Input()],
            [sg.Text('h', size=(8,1), key = 'H'), sg.Input()],
            [sg.Text('k', size=(8,1), key = 'K'), sg.Input()],
            [sg.Button('Graph', size=(8,1), key="graph")],
        ]
        window = sg.Window('asd', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'graph':
                c = calc.conic()
                c.hyperbola(float(values[0]),float(values[1]),float(values[2]),float(values[3]))
                c.show()   
