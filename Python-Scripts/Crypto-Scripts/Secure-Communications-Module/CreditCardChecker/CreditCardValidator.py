# @author Tim McCann
import re
import random


def luhnAlgorithm(cardNumber, a, b):
    numberList = list(map(int, cardNumber)) # converts list of strings to integers
    numberList.reverse() # reverse list of numbers
    oddDigits = 0  # stores the sum of all the odd digits
    evenDigits = 0  # stores the sum of all the even digits
    # loops through all the odd indices in the list and adds the value at that indice to the oddDigits variable
    for x in range(a, len(numberList), 2):
      oddDigits = numberList[x] + oddDigits
    # loops through all the even indices in the list and multiplies the value by two and adds value to evenDigits variable
    for x in range(b, len(numberList), 2):
      add = numberList[x] * 2
      if add > 9:  # if value is greater than 9 then subtract it by 9
          add -= 9
      evenDigits += add
    total = oddDigits + evenDigits  # adds the sum of the odd and even indices
    if total % 10 == 0:  # if mod 10 gives 0, then it's a valid card
        #print("Valid Card Number")
        return True
    else:
        #print("Invalid Card Number")
        return total % 10


CardLength = {
    13 : 'Visa Card',
    19 : 'Visa Card',
    15 : 'American Express Card',
    16 : ['Master Card', 'Visa Card']
}

CardVendors = {
    '^34|37' : 'American Express Card',
    '^51|52|53|54|55|22|27' : 'Master Card',
    '^40|41|42|43|44|45|46|47|48|49' : 'Visa Card'
}


def cardVendor(cardNumber):
    for key in CardVendors:
        match = re.match(key, cardNumber[0:2]) # matches each regex pattern key to first two digits in card number
        if match != None:
            for length in CardLength: # matches length of card number to card length key
                if len(cardNumber) == length:  #
                    if length == 16:
                        for x in CardLength[16]: # since two card type can be 16 in length, loop is created to go through list
                            if x == CardVendors[key]:
                                return CardVendors[key]
                    else:
                        return CardLength[length]



def checksum(ccnumber):
    ccnumberlist = list(map(int, ccnumber)) # converts string to list of integers
    if len(ccnumber) <= 16: # checks to see if length of card is less than or equal to zero
        amount = 16 - len(ccnumber) # stores difference in length between valid and invalid card
        for x in range(amount-1):
            ccnumberlist.append(random.randint(0,9)) # appends random number up to but not including last digit.
        checksum = luhnAlgorithm(''.join(map(str, ccnumberlist)), 1, 0) # returns remainder
        if checksum == 0:
            lastdigit = 0 # if remainder equal to zero then append zero
        else:
            lastdigit = 10 - checksum  # if remainder is greater than zero then minus from 10
        ccnumberlist.append(lastdigit) # append last digit to list
        check = luhnAlgorithm(''.join(map(str, ccnumberlist)), 0, 1) # check to see if it's a valid card
        if check == True:
            print("Valid Card number is " + ''.join(map(str, ccnumberlist)) + " and the checksum is " + str(lastdigit))
        else:
            print("Invalid Card")


MasterCardPrefix = ['51', '52', '53', '54', '55', '22', '27']
AmericanExpressPrefix = ['34', '37']

CardLength2 = {
    'Visa Card':[13,16,19],
    'American Express': [15],
    'Master Card': [16]
}

# ---------------------------------------- Not finished.... (start) ----------------------------------------------------

def randomCreditCardGenertaor(cctype):
    ccnumberlist = []

    if cctype == 'Visa Card':
        ccnumberlist.append('4')
    elif cctype == 'Master Card':
        #prefix =
        ccnumberlist.append(random.choice(MasterCardPrefix))

    elif cctype == 'American Express':
        ccnumberlist.append(random.choice(AmericanExpressPrefix))

    else:
        print("error")


    print(ccnumberlist)

    cclength = 0
    for length in CardLength:
        if cctype == CardLength[length]:
            cclength = length
        else:
            print("error")


    #for length in CardLength:
    for x in range(cclength-2):
        ccnumberlist.append(random.randint(0, 9))  # appends random number up to but not including last digit.
        checksum = luhnAlgorithm(''.join(map(str, ccnumberlist)), 1, 0)  # returns remainder
        if checksum == 0:
            lastdigit = 0  # if remainder equal to zero then append zero
        else:
            lastdigit = 10 - checksum  # if remainder is greater than zero then minus from 10
        ccnumberlist.append(lastdigit)  # append last digit to list
        check = luhnAlgorithm(''.join(map(str, ccnumberlist)), 0, 1)  # check to see if it's a valid card
        if check == True:
            print("Valid Card number is " + ''.join(map(str, ccnumberlist)) + " and the checksum is " + str(lastdigit))
        else:
            print("Invalid Card")

# ----------------------------------------------Not Finished ... (end) -------------------------------------------------

# Uses Luhn Algorithm to validate Credit Card
def validateCreditCard(ccnumber):
    luhn = luhnAlgorithm(ccnumber, 0, 1)
    if luhn != False:
        print("This is a Valid Card Number")
        print("This is a " + cardVendor(ccnumber))
    else:
        print("Invalid Card number, please try again...")






userInput = input("Enter Card Number: ")

#luhnAlgorithm(userInput)

#print(cardVendor(userInput))

#checksum(userInput)

#validateCreditCard(userInput)

randomCreditCardGenertaor(userInput)