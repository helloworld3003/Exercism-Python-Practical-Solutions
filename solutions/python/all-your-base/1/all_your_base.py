def rebase(input_base, digits, output_base):
    def decimal(input_base,digits):
        return sum(digit*(input_base**(len(digits)-1-i)) for i,digit in enumerate(digits))
    if input_base<2:raise ValueError("input base must be >= 2")
    if output_base<2:raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit<0 or digit>=input_base :raise ValueError("all digits must satisfy 0 <= d < input base")
    ten_base=decimal(input_base,digits)
    output=[]
    if output_base==10: return list(int(num) for num in list(str(ten_base)))
    else:
        while ten_base>0:
            output.append(ten_base%output_base)
            ten_base=ten_base//output_base
        return output[::-1] if output!=[] else [0]
