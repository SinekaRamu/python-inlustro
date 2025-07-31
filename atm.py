print("Select the services you want:")
print('1. Withdraw')
print('2. deposit \n3. savings \n4. balance')
PIN = 1234

service = int(input('kindly select: '))

if service == 1:
    print('withdraw')
    amount = int(input('Enter a amount:'))
    
    pin = int(input('Enter your secret pin:'))
    run = True
    while run == 0:     
        if pin == PIN:
            print('collect your amount', amount)
            run = False
        else:
            print('incorrect pin')
    run = True
elif service == 2:
    print('deposit')
elif service == 3:
    print('savings')
elif service == 4:
    print('balance')
else:
    print('kindly select the above services')

