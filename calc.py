
import PySimpleGUI as sg
import math

def cal(text):
    try:
        res = eval(text)
        sg.popup('Result', "{} = {}" .format(text, res))  
    except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")  