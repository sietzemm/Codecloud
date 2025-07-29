# Date of creation 23-10-2018
# Last modified : 24-10-2018
# Author : Sietze Min

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# a list that can contain all the planned activitys
activity_list = []

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('PlannerBoard Application')
    w.show()

    sys.exit(app.exec_())
