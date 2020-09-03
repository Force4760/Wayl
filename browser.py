import webbrowser
from googlesearch import search 
import PySimpleGUI as sg

def search_net(words):
    try:
        for url in search(words, stop=4):
            webbrowser.open_new_tab(url)
    except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")  
        
        