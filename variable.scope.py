#scope = The region that variable is recognized 
# A variable is only available from inside region it is created
#A global and locally scope versions os a variable can be created
name = "Alex" #global scope (available inside e outside functions)
def display_name():
    name = 'Alex'  #local scope (available only inside this function)
    print(name)

display_name()
print(name)


