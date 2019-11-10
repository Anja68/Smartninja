

num1 = int(input("Please enter you first number: "))

num2 = float(input("Please enter you second number: "))


def Multiply(num1, num2):
    if num1 and num2 == float:
        answer = num1 * num2
        return answer
    elif num1 and num2 == int:
        answer = num1 * num2
        return answer
    elif num1 and num2 == str:
        answer = "Bitte Zahl eingeben"
        return answer


print(Multiply(1, 3))



