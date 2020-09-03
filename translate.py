import user_pass as p
from googletrans import Translator
import PySimpleGUI as sg
translator = Translator()


tt = ''
to = ''

def trans(source, lang):
    try:
        translation = translator.translate(source, dest = lang)
        to = translation.origin
        tt = translation.text
        sg.popup('Translation', "{} -> {}" .format(to, tt))
    except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")