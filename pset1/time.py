def main():
    time = input("What time is it darling? : ")
    hours = convert(time)


    if 7 <= hours <= 8 :
        print("Breakfast time bitches")
    elif 12 <= hours <= 13:
        print("Lunch time bitches")
    elif 17 <= hours <= 18:
        print("Dinner time bitches")
  

       

def convert(time):
    hours , minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60 


    ...

if __name__ == "__main__":
    main()