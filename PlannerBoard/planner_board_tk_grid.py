# Date   : 29-10-2018
# Author : Sietze Min

from tkinter import *

class App():
    #Instance variables
    bg_color = '#6699ff'

    def __init__(self,root):
        self.act_list = []
        root.resizable(False,False)
        root.title('PlannerBoard Application')
        self.center_on_screen(root)
        self.init_UI(root)
        self.act_var = 'A first activity!'


    # Creates the user interface
    def init_UI(self,root):
        #Linker gedeelte
        left_menu = Frame(root,bg="blue")
        left_menu.grid(row=0,column=0)

        # Title left part
        lbl1 = Label(left_menu,bg='orange',text="PlannerBoard Application")
        lbl1.grid(row=0,column=0,sticky='S',pady='10px')

        # Buttons left part
        btn1 = Button(left_menu,bg="#6699ff",text="Add Activity",command = self.add_activity).grid(pady=10,row=1,column=0)
        btn2 = Button(left_menu,bg="#6699ff",text="Change Activity",command = self.call_back).grid(pady=10,row=2,column=0)
        btn3 = Button(left_menu,bg="#6699ff",text="Delete Activity",command = self.delete_activity).grid(pady=10,row=3,column=0)
        btn4 = Button(left_menu,bg="#6699ff",text="Button 4",command = self.call_back).grid(pady=10,row=4,column=0)

        # Right part
        right_part = Frame(root,bg='red')
        right_part.grid(row=0,column=1,sticky="N")
        right_part.columnconfigure(0,weight=1,minsize=500)

        lbl3 = Label(right_part,text="Activity list").grid(row=0,column=0,sticky="N")
        self.activity_list = Listbox(right_part)
        self.activity_list.grid(row=1,column=0,pady=8)

        # Footer creation
        footer = Label(root,text="Made by Sietze Min").grid(row=2, column=0,columnspan=2)

    def add_activity(self):
        self.act_list.append(self.act_var)

        for i in self.act_list:
            self.activity_list.insert(END,i)

    def delete_activity(self):
        self.activity_list.delete(0,END)
        self.act_list = []
        # root.update()

    def center_on_screen(self,root):
        w = 600
        h = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - w)/2
        y = (screen_height - h)/2

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def call_back(self):print('Call me back maybe!')


def main():
    root = Tk()
    app = App(root)
    root.mainloop()

main()
