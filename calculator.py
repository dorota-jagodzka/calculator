from os import close
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calculator_logs.log")

def data_for_add_and_substract():
    print("Wprowadzaj ilość liczb, na których chcesz prowadzić działanie")
    total_ammount_of_numbers = int(input())
    ordinal_number = 1
    result = []
    input_data = 0
    
    while ordinal_number <= total_ammount_of_numbers: 
        print("Podaj", ordinal_number, " liczbę")
        input_data = int(input())
        logging.info("Liczba %s to: %s", ordinal_number, input_data )
       
        result.append(input_data)
        ordinal_number = ordinal_number +1
        
    return result

def data_for_multiply_and_divide():
    print("Podaj 1 liczbę")
    num_one = int(input())
    print("Podaj 2 liczbę")
    num_two = int(input())

    return num_one, num_two


def add():
    logging.info("Wybrano dodawanie.")
    numbers = data_for_add_and_substract()
    
    return sum(numbers)

def substract():
    numbers = data_for_add_and_substract()
    logging.info("Wybrano odejmowanie.")
    first_number = numbers[0]

    return first_number - sum(numbers[1:])

def multiply():
    logging.info("Wybrano mnożenie.")
    number_one, number_two = data_for_multiply_and_divide()

    return number_one * number_two

def divide():
    logging.info("Wybrano dzielenie.")
    
    number_one, number_two = data_for_multiply_and_divide()

    return number_one / number_two

def problem(): 
    logging.error("Nieprawidłowy format wpisywanych liczb. ")
    print("Nieprawidłowy format wpisywanych liczb. ")
    quit()


############################# MAIN ############################# 
logging.debug("")
logging.debug("------------------------")
logging.debug("NOWE DZIAŁANIE")
logging.debug("------------------------")


print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
options = { 1: add, 2: substract, 3: multiply, 4: divide }

final_result = options.get(int(input()), problem)()
   

print("Wynik to: ", final_result)
logging.debug("Wynik to: %s" % final_result)
logging.debug("------------------------")
logging.debug("KONIEC DZIALANIA")
logging.debug("------------------------")
logging.debug("")