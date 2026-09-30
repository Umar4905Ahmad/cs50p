def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))        

def convert(fraction):
    x , y = fraction.split("/")
    x = int (x)
    y = int (y)
    if x > y :
        raise ValueError 
    return round(x / y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 90 :
        return "F"
    return f"{percentage}%"


main()