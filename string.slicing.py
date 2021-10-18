# slicing = create a substring by extracting elements from another string 
#          indexing[] or slice()
#          [start:stop:step]

name = 'Maria Padilha'
first_name = name[0:5]
last_name = name[6:13]
funky_name = name[0:13:1]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "https://google.com"


slice = slice(7,-4)
print(website1[slice])
