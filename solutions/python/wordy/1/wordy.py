def answer(questionaire):
    question=questionaire
    question = question.replace(" ","").replace("?","").replace("Whatis","")
    print(question)
    j = 0
    result = 0
    operator = []
    number = []
    if "cubed" in question: raise ValueError("unknown operation")
    
    # If it ends with something that isn't a digit, it's invalid
    if len(question)==0 or (not question[-1].isdigit()):
        raise ValueError("syntax error")
            
    i = 0
    while i < len(question):
        # Find the start of an operator (a letter)
        if question[i].isalpha() and question[j:i]:
            # We hit a letter, so save the number we just passed
            number.append(question[j:i])
            
            # Now detect which operator it is and update i
            if question[i:i+4] == "plus":
                operator.append("+")
                i += 4
            elif question[i:i+5] == "minus":
                operator.append("-")
                i += 5
            elif question[i:i+12] == "multipliedby":
                operator.append("*")
                i += 12
            elif question[i:i+9] == "dividedby":
                operator.append("/")
                i += 9
            else:
                raise ValueError("syntax error")
            
            j = i # move `j` to start of the next number
        else:
            i += 1
            
    # Append the final number
    if j < len(question):
        number.append(question[j:])
    if not all(num in questionaire for num in number): raise ValueError("syntax error")
    
    # Calculate result left-to-right
    result = int(number[0])
    for i in range(1, len(number)):
        # eval is generally unsafe, but matches your logic:
        result = eval(str(result) + operator[i-1] + number[i])
        
    return result

print(answer("What is -5?"))
