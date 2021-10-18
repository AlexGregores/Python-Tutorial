# str.format() = optional method that gives users
# more control when displaying output

animal = "cow"
item = "moon"

#print("The " , animal ,"jumped over the", item)
#print("The {} jumped over the {}".format("animal","item"))
#positional arguments
#print("The {1} jumped over the {0}".format("animal","item"))#keyword argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

text = "the {} jumped over the {}"
print(text.format(animal,item))

name = "Alex"
print("Hello, my name is {}".format(name))
print("Hello,my name is {:10}. Nice to meet you!".format(name))
print("Hello,my name is {:<10}. Nice to meet you!".format(name))
print("Hello,my name is {:>10}. Nice to meet you!".format(name))
print("Hello,my name is {:^10}. Nice to meet you!".format(name))

number = 1000
print("The number PI is {:.3f}".format(number))
print("The number  is {:,}".format(number))
print("The number  is {:b}".format(number))
print("The number  is {:o}".format(number))
print("The number  is {:x}".format(number))
print("The number  is {:e}".format(number))





