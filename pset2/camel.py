def camel() :
    name = input("Camel case : ")
    print("Snake case: ",snake(name))

def snake(name):
    entered_words= ""
    for char in name :
        if char.isupper():
            entered_words += "_" + char.lower()

        else :
            entered_words += char
    return entered_words

if __name__ == "__main__":
    camel()