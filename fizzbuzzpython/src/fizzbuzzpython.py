def calculateFizzBuzz(startNumber, endNumber):    
    result = ""
    for number in range(startNumber, endNumber + 1):
        result += calculateFizzBuzzForANumber(number)
        
    print result
        
def calculateFizzBuzzForANumber(number):
    result = str(number) + " : "
    value = ""
    if (number % 3 == 0):
        value = "Fizz"
    
    if (number % 5 == 0):
        value += "Buzz"
        
    if ("" == value) :
        value = str(number)
        
    result += value + "\n"
    
    return result

startNumber = input('Enter start number')
endNumber = input('Enter end number')

calculateFizzBuzz(startNumber,endNumber)