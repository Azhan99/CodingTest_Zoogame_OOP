from random import randint
import tkinter as tk
from datetime import datetime,timedelta

#Defining Classes
class Animal:
  def __init__(self,name) -> None:
    self.name=name
    self.health=100
    self.state='alive'


  def set_state(self,new_state):
    self.state=new_state


  def set_health(self,number):
    if self.state!='dead':
        self.health=self.health + number
    
    if self.health>100:
      self.health=100

    if self.health<0:
        self.health=0

  def check_status(self):
    if self.name=='Elephant':
        if self.health>=70:
            return self.set_state('alive')
        if self.health<70 and self.state=='cannot walk':
            return self.set_state('dead')
        elif self.health<70 and self.state!='dead':
            return self.set_state('cannot walk')
    
    if self.name=='Monkey':
        if self.health<30:
            return self.set_state('dead')

    if self.name=='Giraffe':
        if self.health<50:
            return self.set_state('dead')



class Elephant(Animal):
    def check_health(self):
        return super().check_status()
  

class Monkey(Animal):
    def check_health(self):
        return super().check_status()

class Giraffe(Animal):
    def check_health(self):
        return super().check_status()

#Functions
def Add_time():
    global now
    now+=timedelta(hours=1)
    label_currenttime.config(text='Time:   '+now.strftime("%H:%M"))

    for types,animal_label in animal_list:
        damage_amount=randint(0,20)
        types.set_health(-damage_amount)
        types.check_health()
        animal_label.config(text=f'{types.name} (Health: {types.health}, State: {types.state})')


#Creating time
now=datetime.now()
currentTime = now.strftime("%H:%M")

#Creating five animals of each category
N=5
elephant=[Elephant(f'Elephant') for i in range(N)]
monkey=[Monkey(f'Monkey') for i in range(N)]
giraffe=[Giraffe(f'Giraffe') for i in range(N)]
#Creating a list of all animals
animals=[elephant,monkey,giraffe]

#Button for feeding
def feed():
    for types,animal_label in animal_list:
        feed_amount=randint(10,25)
        types.set_health(feed_amount)
        types.check_health()
        animal_label.config(text=f'{types.name} (Health: {types.health}, State: {types.state})')


#Creating GUI
root = tk.Tk()
root.title("Zoo game")
root.geometry("700x700")
#Placing time
label_currenttime = tk.Label(root, text='Time:   '+now.strftime("%H:%M"))
button_time = tk.Button(root, text='Increment Hours', width=25, command=Add_time)
button_time.pack()
#Placing animals
Feed_button=tk.Button(root,text='Feed', width=15, command=feed)
Feed_button.pack()
#List to collect labels and types
animal_list=[]
for animal in animals:
    for types in animal:
        animal_label = tk.Label(root, text=f'{types.name} (Health: {types.health}, State: {types.state})')
        animal_list.append((types,animal_label))
        animal_label.pack()
#packing
root.mainloop()