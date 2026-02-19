#recursion(head recoursion (print kartik 4 times ))
count = 0
def name():
                    global count #tell the python global count var use in inside the function .
                    if count == 4:
                            return 
                    print("kartik")
                    count += 1
                    name()
name()



# Tell recursion(backtraking (print kartik 4 times ))
count = 0 
def name():
        global count 
        if count == 4:
                return 
        count += 1
        name()
        print("kartik")
name()