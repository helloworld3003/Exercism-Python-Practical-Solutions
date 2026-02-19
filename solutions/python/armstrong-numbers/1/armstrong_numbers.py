def noofdigits(number):
    i=0
    while number>0:
        number=number//10
        i+=1
    return i
def is_armstrong_number(number):
    total=0
    number1=number
    while number1>0:
        digit=number1%10
        number1=number1//10
        total=total+digit**noofdigits(number)
    return total==number