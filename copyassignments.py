import os
import shutil

# simple script to organize the desktop  

def stu_activities():
    for dir in os.listdir("/Users/Desktop"):
        assignments = "assignments"
        if os.path.exists(assignments) != True:
            os.mkdir(assignments)
        if dir.startswith("Stu_"):
            path = os.path.join("/Users/Desktop", dir)
            shutil.move(path, assignments)
            

stu_activities()
