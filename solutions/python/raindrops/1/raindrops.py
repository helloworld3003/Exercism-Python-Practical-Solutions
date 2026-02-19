def convert(number):
    result=""
    if any(number%i==0 for i in [3,5,7]):
        if number%3==0: result=result+"Pling"
        if number%5==0: result=result+"Plang"
        if number%7==0: result=result+"Plong"
    else: result=result+str(number)
    return result
