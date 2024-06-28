import random

# seting a function where it takes 3 arguments: min, max and quantity
# min - minimal possible number (not less than 1)
# max - maximum possible number (not more than 1000)
# quantity - amount of numbers we have to choose within min and max numbers
def get_number_tickets(min, max, quantity) -> list: 
    list_of_numbers = [] # the function supposed to return list of numbers. All collection is goint to be placed in the list_of_numbers
    