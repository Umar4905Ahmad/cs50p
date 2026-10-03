import inflect

p = inflect.engine()

names = []

while True :
    try :
        names.append(input("Enter the names: "))
    except EOFError : 
        print()
        break 

print("Adieu, Adieu, to" + p.join(names))

