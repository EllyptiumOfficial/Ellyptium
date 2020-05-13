from os import system, remove

def otg_code(code, mode = "cmdfast", name = "untitled", path = "", writemode = "w"):

    if mode == "cmdfast" or mode == None:
        system(f'cmd /c "{code}"')

    elif mode == "cmdkeep":
        system(f'cmd /k "{code}"')
    
    elif mode[:6] == "python":

        if path != "":
            otgfile = open(f"{path}\\{name}.py", writemode)
        
        else:
            otgfile = open(f"{name}.py", writemode)
        

        if type(code) == str:
            otgfile.write(code)
        
        else:
             otgfile.writelines(f"{l}\n" for l in code)

        otgfile.close()

        if mode[-4:] ==  "keep":
            system(f"python {name}.py")

        elif mode[-4:] == "fast":
            system(f"python {name}.py")
            remove(f"{name}.py")