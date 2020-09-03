import PySimpleGUI as sg
import calc as cal
import create_linux as cr
import translate as t
import browser as b
import pickle
import timing as ti
import wiki as w

google_keys = "search"
create_keys = "create"
translate_keys = "translate"
wiki_keys = "wiki"
calc_keys = "calc"
dict_keys = "meaning"
time_keys = "time"

class Tela:
    
    

    def __init__(self):
        
        layout = [
            [sg.Text("Hi! I'm WAYL.")],
            [sg.Text("How can I help you?")],
            [sg.Text("Command"), sg.Input()],
            [sg.Button("Execute"), sg.Button("Settings"), sg.Button("Help")],
        ]
        
        window = sg.Window("Wayl").layout(layout)
        self.event, self.command = window.Read()
        
    def settings(self):
        
        layout2 = [
            [sg.Text("GitHub Key"), sg.Input()],
            [sg.Button("Save")]
        ]
        
        settings = sg.Window("Settings").layout(layout2)
        
        self.event, self.command = settings.Read()
        
        if self.event == "Save":
            pickle.dump(self.command[0], open('github.dat', 'wb' ))
            
    def start(self, text):
        text = text.strip()

        if text.startswith(calc_keys):
            text = text.replace(calc_keys, '')
            text = text.strip()
            cal.cal(text)

        elif text.startswith(wiki_keys):
            text = text.replace(translate_keys, '')
            text = text.strip()
            textargs = text.split("-")
            text0 = textargs[1].replace('-', '')
            text0 = text0.strip()
            w.wikicall(text0)

        elif text.startswith(translate_keys):
            text = text.replace(translate_keys, '')
            text = text.strip()
            textargs = text.split("-")
            text0 = textargs[1].replace('-', '')
            text0 = text0.strip()
            text1 = textargs[2].replace('-', '')
            text1 = text1.strip()
            t.trans(text0, text1)

        elif text.startswith(create_keys):
            text = text.replace(create_keys, '')
            text = text.strip()
            textargs = text.split("-")
            text0 = textargs[1].replace('-', '')
            text0 = text0.strip()
            text1 = textargs[2].replace('-', '')
            text1 = text1.strip()
            cr.create(text0, text1)
            
        elif text.startswith(google_keys):
            text = text.replace(google_keys, '')
            text = text.strip()
            textargs = text.split("-")
            b.search_net(textargs[1])
        
        elif text.startswith(time_keys):
            ti.telltime()
            
        else:
            sg.popup('Sorry', "Something went wrong!\nTry again please!")  

        


while True:
    
    win = Tela()
    
    if win.event == "Execute":
        win.start(win.command[0])
        
    elif win.event == "Help":
        sg.popup('Help', "time -> tell time\n   ex: time\n \nsearch -> google search\n   ex: search -vscode\n \ntranslate -$origin -$tolang -> translate a word\n   ex: translate -I am -pt\n \nwiki - search on wikipedia\n   ex: wiki -music\n \ncalc $calculation -> calculate (python)\n   ex: calc 2+5\n \ncreate -$name -$type -> create a new project\n   ex: create -new project -(web/flutter/python/design/music)\n")
    
    elif win.event == "Settings":
        win.settings()
    
    if win.event == sg.WIN_CLOSED:
        break  
