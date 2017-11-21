print("hello world")
name = input("what is your name? ")
age = str(input("how old are you? "))
print("hello", name, age) #comma outputs direct result
print("hello" + name + age) #plus tries to construct a string to display, and it will only work with in if it is converted to str manually
print("hello {0} you are {1} years old".format(name, age))