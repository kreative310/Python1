
try :
    result = 10/0
    print(result)

except ZeroDivisionError :
    print()



  fruits {
      "banana" : 10,
      "apple" : 7,
      "cherry" : 3
  }

  try :
      print(fruits[avocado])


     text = "this is not a number"
try :

    text_to_int =  Int(text)
except Exeption as e :
     print("an error has occured", e)


try :
    result = 10/ 3

except ZeroDivisionError:
    print("was not succesful")

else:
    print("was succesful", result)


try :
    result = 10/2

except:
    print()

finally:
    print()


num1 = 5
num2 = 3

result =  num1 + num2
print(result)

if :
 result = 10
 print("it is the number we are looking for", result)

else :
    print("wrong")

except 9 :
print(error)

def perform_operation(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operator"

# Example usage
result = perform_operation(10, 5, '+')
print(result)  # Output: 15

user_input = input("Enter a decimal number: ")
number = float(user_input)  # typecast to float
print("The decimal number is:", number)

