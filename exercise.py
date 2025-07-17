# stringInput = input("enter the string of numbers: ")
# resultInput = input(int("enter a number: "))

stringInput = "1234567"
resultInput = -2
totalNumbers = len(stringInput)
found = False


def backTrack(i, currentResult):
    global found
    if i == totalNumbers:
        if currentResult == resultInput:
            found = True
        return

    digit = int(stringInput[i])
    
    backTrack(i + 1, currentResult + digit)

    backTrack(i + 1, currentResult - digit)


firstDigit = int(stringInput[0])
backTrack(1, firstDigit)
backTrack(1, -firstDigit)

if found:
    print("yes")
else:
    print("no")
