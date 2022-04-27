with open('currencyValues.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.split('\t')
    currencyDict[parsed[0]] = parsed[1]

userAmt = int(input('Enter the amount : '))

[print(item) for item in currencyDict.keys()]

userCurrency = input('Enter the Country you want to change : ')

print(f'{userAmt} INR is {userAmt*float(currencyDict[userCurrency])} {userCurrency}')