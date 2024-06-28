import random

# seting a function where it takes 3 arguments: min, max and quantity to create a list of unique numbers within chosen range.
# min - minimal possible number (not less than 1)
# max - maximal possible number (not more than 1000)
# quantity - amount of numbers we have to get within min and max numbers.
def get_number_tickets(min, max, quantity) -> list: 

    list_of_numbers = [] # the function supposed to return list of numbers. The desired collection is going to be placed in the list_of_numbers.
    
    # check if the information was typed in correctly on a user side, no string or float numbers,
    # also check if min number is not bigger than max or quantity is not bigger than min and max difference
    try:    
        min = int(min)  # converting all values into int type to check for exceptions first
        max = int(max)
        quantity = int(quantity)
                
        if min <= 0 or max >= 1000 or quantity > (max - min + 1) or min >= max: #check if the information was typed in correctly on a user side and meet our conditions
            print("Please, write minimal and maximum numbers, along with the quatity of numbers in the list. They supposed to be natural in range within 1 and 1000.")
            return []
        
        # if all conditons are met, creating a list with unique numbers of the desired quantity within chosen range:
        list_of_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(list_of_numbers)  #sorting out the list and return as a final solution
        
    except ValueError: #check if the information was typed in correctly on a user side, working on exception of the vrong value
        print("Please, write minimal and maximum numbers, along with the quatity of numbers in the list. They supposed to be natural in range within 1 and 1000.")
        None
        return []
    except TypeError: #check if the information was typed in correctly on a user side, orking on exception if the srting type was typed in and it's impossible to convert into integer
        print("Please, write minimal and maximal numbers, along with the quatity of numbers in the list. They supposed to be natural in range within 1 and 1000.")
        None
        return []

'''    
# example usage:
min = input("Please, write minimal number: ")
max = input("Please, write maximal number: ")
quantity = input("How many numbers do you want to get? - ")

print(get_number_tickets(min, max, quantity))
'''