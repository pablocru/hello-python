# Input a number
num = input('Input a number?\n')

# Casting the response to number
num = float(num)

# Get the number type
if num > 0:
    numType = 'positive'
elif num == 0:
    numType = 'zero'
else:
    numType = 'negative'

# Tell the user what type of number it is
print(num, 'is', numType)
