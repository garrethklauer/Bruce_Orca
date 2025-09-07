import os
import sys
import ctypes

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
def RunThroughDir():
    os.chdir("c:/")
    Dir = os.listdir()
    
    index = -1
    count = 0
    while index < len(Dir):
        print(Dir[index])
        index += 1
        count += 1
        current_dir = Dir[index]
        try:
            os.chdir("c:/" + str(current_dir) + "/")
            with os.scandir("c:/" + str(current_dir) + "/") as entries:
                for entry in entries:
                    if entry.is_dir() == True:
                        os.chdir("c:/" + str(current_dir) + "/" + str(entry.name) + "/")
        except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
            print(f"cant open: {current_dir} - {e}")
            index += 1
            continue            
        print(os.listdir("c:/" + str(current_dir) + "/"))
        



        

RunThroughDir()
        
        

