import os
import shutil

def stu_activities():
    for dir in os.listdir("/Users/kevinheredia/Desktop"):
        assignments = "assignments"
        if os.path.exists(assignments) != True:
            os.mkdir(assignments)
        if dir.startswith("Stu_"):
            path = os.path.join("/Users/kevinheredia/Desktop", dir)
            shutil.move(path, assignments)
            

stu_activities()