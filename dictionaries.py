# dictionary = A changeable, unordered collection of unique key:value pairs fast becouse they use hashing, allow us to access a value quickly

capitals = {
    'USA':'Washington',
    'India':'New Dehli',
    'China':'Beijing',
    'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'}) #update item
capitals.pop('China') #remove item
capitals.clear() # remove everthing
#print(capitals['China'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,value)
