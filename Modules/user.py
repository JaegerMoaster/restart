
def division(x,y):
    try:
        return x/y
    except:
        if(not y>0 and not y<0):
            return "No division by zero allowed"
        
        elif(not isinstance(x, int) or not isinstance(y, int)):
            return "Wrong input type for : " + str(x) + " & " + str(y)
        
        else:
            return "You screwed up completely"

print(division("text",1))