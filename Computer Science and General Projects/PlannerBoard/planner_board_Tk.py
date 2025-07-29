# Date of creation 23-10-2018
# Last modified : 26-10-2018
# Author : Sietze Min

import sys
from tkinter import *

# a list that can contain all the planned activitys

class App:
    #Instance variables
    bg_color = '#6699ff'

    def __init__(self,root):
        root.resizable(False,False)
        root.title('PlannerBoard application')
        self.activity_list = []

        # frame_main = PanedWindow(root,width=400,height=400,orient=HORIZONTAL,bg='#6699ff')
        # frame_main.pack(fill=None, expand=False)

        frame_left = PanedWindow(root,width=200,height=400,orient=HORIZONTAL,bg='red')
        frame_left.pack(side=LEFT,fill=BOTH, expand=False)

        frame_right = PanedWindow(root,width=600,height=40,orient=HORIZONTAL,bg='#6699ff')
        frame_right.pack(side=RIGHT,fill=BOTH,expand=False)

        frame_bottom = PanedWindow(frame_right,width=600,height=20,bg='#000')
        frame_bottom.pack(side=BOTTOM,fill=BOTH,expand=False)

        # l1 = Label(frame_left, text="Hello")
        # l1.pack()

    # add an activivty
    def add_act(self,name):
        current_acivity = name
        activity_list.append(current_acivity)
        return 'activity added!'

    # Remove an activity
    def remove_act(self,name):
        current_acivity = name
        activity_list.pop(current_acivity)

    # Change an activity
    def change_act(self,name):
        current_acivity = name
        # current.activity.name = current_acivity
        return current_acivity,'has been updated!'

root = Tk()
app = App(root)
root.mainloop()
