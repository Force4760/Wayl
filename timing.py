import PySimpleGUI as sg
import datetime as dt



def telltime():
    try:
        now = dt.datetime.now()
        print(now)
        sg.popup('Time', "Current Time -> {}" .format(now))
    except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!") 
