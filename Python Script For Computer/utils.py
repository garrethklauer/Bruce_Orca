import os

def RunThroughDir():
    os.chdir("c:/")
    Dir = os.listdir()
    
    index = 0
    count = 0
    while index + 1 < len(Dir):
        print(Dir[index])
        index += 1
        count += 1
        current_dir = Dir[index]
        #for i in range(index):
        try:
            os.chdir("c:/" + str(current_dir) + "/")
        except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
            print(f"cant open: {current_dir} - {e}")
            index += 1
            continue            
        print(os.listdir("c:/" + str(current_dir) + "/"))

        

RunThroughDir()
        
        

