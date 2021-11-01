from os import close
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calculator_logs.log")

def dataForAddAndSubstract():
    print("Wprowadzaj kolejno liczby zatwierdzając Enterem. Wpisując 0 kończysz wprowadzanie.")
    inputData = 1
    result = []
    count = 1;
    while(inputData !=0):
        print("Podaj", count, " liczbę")
        inputData = int(input()) 
        logging.info("Liczba %s to: %s", count, inputData )
        result.append(inputData)
        count = count +1
    
    return result

def dataForMultiplyAndDivinde():
    print("Podaj 1 liczbę")
    numOne = int(input())
    print("Podaj 2 liczbę")
    numTwo = int(input())

    return numOne, numTwo

def add(numbers):
    logging.info("Wybrano dodawanie.")

    return sum(numbers)

def substract(numbers):
    logging.info("Wybrano odejmowanie.")
    firstAndFinalNumber = numbers[0]

    return firstAndFinalNumber - sum(numbers[1:])

def multiply(numberOne, numberTwo):
    logging.info("Wybrano mnożenie.")

    return numberOne * numberTwo

def divine(numberOne, numberTwo):
    logging.info("Wybrano dzielenie.")

    return numberOne / numberTwo


############################# MAIN ############################# 
logging.debug("")
logging.debug("------------------------")
logging.debug("NOWE DZIAŁANIE")
logging.debug("------------------------")

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
finalResult = 0
selectNumber = int(input())
if selectNumber == 1:
    listOfNumbers = dataForAddAndSubstract()
    finalResult = add(listOfNumbers)
elif(selectNumber == 2):
    listOfNumbers = dataForAddAndSubstract()
    finalResult = substract(listOfNumbers)
elif(selectNumber == 3):
    numOne, numTwo = dataForMultiplyAndDivinde()
    finalResult = multiply(numOne, numTwo)
elif(selectNumber == 4):
    numOne, numTwo = dataForMultiplyAndDivinde()
    finalResult = divine(numOne, numTwo)
else:
    logging.error("Nieprawidłowy format wpisywanych liczb. ")
    print("Nieprawidłowy format wpisywanych liczb. ")
    quit()

print("Wynik to: ", finalResult)
logging.debug("Wynik to: %s" % finalResult)

logging.debug("------------------------")
logging.debug("KONIEC DZIALANIA")
logging.debug("------------------------")
logging.debug("")