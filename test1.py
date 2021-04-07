Age=int(input('Enter your age:'))

if Age>=30:
    print('You are aged')
else:
    print("sexy age\nLet's have a date")
    if Age<=30:
        if(input('Are you interested, say Y or N')=='Y'):
            print('Awsome')
    print('Good luck')