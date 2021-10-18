# logical operators (and, or, not) = used to check if two or more conditional statement is true

temp = int(input("What's the temperature out side?:"))

if temp >=0 and temp <=30:
    print('the temperature is good today!')
    print('Go outside')
elif temp < 0 or temp > 30:
    print('the temperature is bad today')
    print('stay inside!')
#if not(temp >=0 and temp <=30):
#    print('the temperature is bad today')
#   print('stay inside!')
#elif not(temp < 0 or temp > 30):
    
#   print('the temperature is good today!')
#    print('Go outside')


