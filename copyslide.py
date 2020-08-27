import os
import shutil

def pptx_copy():
    for file in os.listdir("/Users/kevinheredia/Downloads"):
        powerpointfile = "powerpoint files"
        if os.path.exists(powerpointfile) == False:
            os.mkdir(powerpointfile)
        if file.endswith(".pptx"):
            path = os.path.join("/Users/kevinheredia/Downloads/", file)
            shutil.copy(path,powerpointfile)
        if file.endswith(".ppt"):
            path = os.path.join("/Users/kevinheredia/Downloads/", file)
            shutil.copy(path,powerpointfile)

pptx_copy()
            