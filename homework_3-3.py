import re   # importing re module for advance operationg with strings 

# creating a function, which takes the string typed phone number, gets rid of all excessive symbols, except "+",
# and adding a country area if missing, forming it into a normalized way of presenting, according to our conditions:
def normalize_phone(phone_number) -> str:
    try:
        phone_number = re.sub(r"\s+", "", phone_number)                 # removing all excessive spaces, inside ad outside the phone number
        phone_number = re.sub(r"[\\t\\n\\r\\f\\v]", "", phone_number)   # removing all tabulation symbols
        phone_number = re.sub(r"[;,\-:!\.()\\]", "", phone_number)      # removing all symbols ecxept "+"
        
        if phone_number[0] != "+":                                      # adding "+" at the beggining of the phone number if doesn't exist:
            phone_number = re.sub(r"^0|^380", "380", phone_number)      # 1) setting beggining "380" by default if the number beggins with 0 or 380
            phone_number = re.sub(r"^", "+", phone_number)              # 2) adding "+" at the beggining of the phone number
        
        if len(phone_number) > 13:                                      # checking if the length of the phone number is correct, no excessive digits
            print(f"{phone_number} has too many symbols. Please, check if you are not mistaken")
            return ""
        elif len(phone_number) < 13:                                    # checking if there's enough digits in the phone number
            print(f"{phone_number} has not enough symbols. Please, check if you are not mistaken")
            return ""


        int(phone_number[1:-1])                                         # checking if all digits are convertable into numbers, calling an exception if not
        
        return phone_number                                             # if all conditions are met, returning phone_number as a string
    
    except ValueError:                                                  # returning an empty string if any digit is not a number
        print(f"{phone_number} is a wrong number, supposed to content only integer digits, except '+' at the beggining")
        return ""
        


'''
# example of usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 47 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
'''