#this function converts degrees in fahrenheit to celsius
def ftoc():
    f = int(input("Enter Degrees in fahrenheit: "))
    cl = (f-32)*5/9
    print(f,"degrees fahrenheit converts to",cl,"degrees celsius")

#this function converts distance in miles to kilometres
def mtk():
    m = int(input("Enter distance in Miles: "))
    k = (m*1.6)
    print(m,"is",k,"kilometres")

#this function converts distance in inches in inches to centimeters
def itc():
    i = int(input("Enter distance in Inches: "))
    c = (i*2.54)
    print(i,"is",c,"centimeters")

#######################################################################################

def menu():
    choice = '0'
    while choice == '0':
        print("1 | Fahrenheit to Celsius Converter")
        print("2 | Mile to Kilometre Converter")
        print("3 | Inch to Centimeter Converter")
        choice = input("Please make a choice: ")
        if choice == "4":
            print("Quitting...")
            break
        elif choice == "1":
            ftoc()
            menu()
        elif choice == "2":
            mtk()
            menu()
        elif choice == '3':
            itc()
            menu()
        else:
            print("I dont understand your input")
            menu()
menu()

