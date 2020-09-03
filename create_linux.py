import os
import subprocess
from github import Github
import user_pass as p
import PySimpleGUI as sg
import pickle




            

def crepo():
  gi = pickle.load(open('github.dat', 'rb')) 
  user = Github(gi).get_user()
  repo = user.create_repo(name)
  subprocess.call('git init', shell=True)
  subprocess.call('touch README.md', shell=True)
  subprocess.call('git add README.md', shell=True)
  subprocess.call('git remote add origin git@github.com:Force4760/{}.git' .format(name), shell=True)
  subprocess.call("git commit -m 'firstcommit'" , shell=True)
  subprocess.call("git push -u origin master" , shell=True)
  subprocess.call("code ." , shell=True)

  

def create(name, category):
    if category == "design":
      try:
        path = os.path.join("/media/force/Sample_Vst/FORCE/_DESIGN/Projects", name)
        assets = os.path.join(path, "Assets")
        finals = os.path.join(path, "Finals")
        os.mkdir(path)
        os.mkdir(assets)
        os.mkdir(finals)
        subprocess.Popen(r'explorer /select, {}' .format(assets))
      except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")

    elif category == "web":
      try:
        path = os.path.join("/media/force/Sample_Vst/FORCE/_CODING/Web/Projects", name)
        images = os.path.join(path, "images")
        styles = os.path.join(path, "styles")
        os.mkdir(path)
        os.mkdir(images)
        os.mkdir(styles)
        os.chdir(path)
        crepo()
      except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")
      
    elif category == "flutter":
      try:
        path = os.path.join("/media/force/Sample_Vst/FORCE/_CODING/Flutter/Projects", name)
        images = os.path.join(path, "images")
        fonts = os.path.join(path, "fonts")
        os.mkdir(path)
        os.mkdir(images)
        os.mkdir(fonts)
        os.chdir(path)
        crepo()
      except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")

    elif category == "python":
      try:
        path = os.path.join("/media/force/Sample_Vst/FORCE/_CODING/Python/Projetos", name)
        os.mkdir(path)
        os.chdir(path)
        crepo()
      except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")
    
    elif category == "design":
      try:
        path = os.path.join("/media/force/Sample_Vst/FORCE/_DESIGN/Projects", name)
        stems = os.path.join(path, "Stems")
        tracks = os.path.join(path, "Tracks")
        samples = os.path.join(path, "Samples")
        os.mkdir(path)
        os.mkdir(stems)
        os.mkdir(tracks)
        os.mkdir(samples)
        subprocess.Popen(r'explorer /select, {}' .format(stems))
      except:
        sg.popup('Sorry', "Something went wrong!\nTry again please!")

    else:
      sg.popup('Sorry', "Something went wrong!\nTry again please!")
    
