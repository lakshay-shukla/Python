# 2. Menu Driven Program
Pin = int(input('Enter your Pin: '))

if Pin == 1234:
    print('Your Welcome!')
    menu = input('''Hi How can I help you?
       1. Pin Change
       2. Withdrawal
       3. Balance Check
       4. Exit
       ''')
    if menu == '1':
        print('Change Your Pin')
        New_Pin = int(input('Enter your new Pin: '))
    elif menu == '2':
        print('Withdrawal Your money')
        Amount = int(input('Enter your amount: '))
    elif menu == '3':
        print('Balance Check')
    else:
        print('Exit')
else:
    print('Please enter a valid Pin')