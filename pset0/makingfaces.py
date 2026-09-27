def convert(text):
    result = text.replace(":)", "🙂")
    result = result.replace(":(", "🙁")
    return result 

def main():
    text  = input()
    output  = convert(text)
    print(output)

main()