import wikipedia
import PySimpleGUI as sg


def wikicall(text):
    try:
        su = wikipedia.summary(text, sentences=3)  
        sg.popup('Result', su)
    except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")  