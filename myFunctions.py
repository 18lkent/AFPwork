#create a main function that runs when this file is executed
def main():
    print('hello')
    print("This program will ask you for a temperature\n in Fahrenheit")
    print("____________________________________________")

#create a function to convert fahrenheit to celcius
def ftoc():
    f = int(input("Enter Degrees in fahrenheit: "))
    cl = (f-32)*5/9
    print(f,"degrees fahrenheit converts to",cl,"degrees celsius")

main()
ftoc()
