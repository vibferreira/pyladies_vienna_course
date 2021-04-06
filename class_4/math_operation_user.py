input_number1 = float(input("Input the first number: "))
input_number2 = float(input("Input the second number: "))
input_operator = input("Input an operator (+,-,* or /): ")

if input_operator == "+":
    output = input_number1 + input_number2
    print("The output is: ", output)
elif input_operator == "-":
    output = input_number1 - input_number2
    print("The output is: ", output)
elif input_operator == "*":
    output = input_number1 * input_number2
    print("The output is: ", output)
else:
    output = input_number1 / input_number2
    print("The output is: ", output)


