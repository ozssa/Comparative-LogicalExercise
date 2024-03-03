'''
#Todo:
+ = True
- = False

1. -----0+++++5-----8+++++11-----
2. +++++0-----5+++++8-----11+++++
'''

print('\n=================================')
print('1. -----0+++++5-----8+++++11-----\n2. +++++0-----5+++++8-----11+++++')
print('=================================')

ProblemNumber = int(input('Enter Problem Number: '))
UserInput = float(input("Enter a Number: "))

if ProblemNumber == 1:
    isGreaterThan0 = UserInput > 0
    isLessThan5 = UserInput < 5
    isGreaterThan8 = UserInput > 8
    isLessThan11 = UserInput < 11
    IsCorrect = (isGreaterThan0 and isLessThan5) or (isGreaterThan8 and isLessThan11)
    print('Your Number:', IsCorrect)

elif ProblemNumber == 2:
    isLessThan0 = UserInput < 0
    isGreaterThan5 = UserInput > 5
    isLessThan8 = UserInput < 8
    isGreaterThan11 = UserInput > 11
    IsCorrect = isLessThan0 or (isGreaterThan5 and isLessThan8) or isGreaterThan11
    print('Your Number:', IsCorrect)

else:
    print('Invalid Problem Number')
