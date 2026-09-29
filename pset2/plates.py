def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not correct_length(s):
        return False
    if not only_letters_and_numbers(s):
        return False
    if not starts_with_letters(s):
        return False
    if not numbers_at_end(s):
        return False
    return True

    
def correct_length(s):
    if len(s) < 2 or len(s) > 6 :
        return False
    
    return True

def only_letters_and_numbers(s):
    return s.isalnum()

def starts_with_letters(s):
    return  s[:2].isalpha()

def numbers_at_end(s):
    seen_digit = False
    for char in s:
        if char.isdigit():
            if not seen_digit and char == "0":
                return False
            seen_digit = True
        else:
            if seen_digit:
                return False
    return True

main()
