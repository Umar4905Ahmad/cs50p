expression = input("Enter the charcters you want :")
x , y , z = expression.split()
x= int(x)

z= int(z)

if y ==  "+":
    result = (x + z)
elif y == "-":
    result = (x - z)
elif y == "/":
    result = (x / z)
elif y == "*":
    result = (x * z)
else :
    print("you missed the operator!")


print(f"{result :.1f}")

