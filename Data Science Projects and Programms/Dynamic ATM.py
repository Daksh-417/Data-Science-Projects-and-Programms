import Bank_Balance
print('\t\t\t\t Welcome to KotaK ATM')
pin = 1234
if input('Insert your card: ') == 'card':
    print('Welcome')
    if pin == int(input('Enter your pin: ')):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('1) Check Balance\t\t2) Withdraw\t\t3) End transaction\n')
        option = int(input('Select your option: '))
        if option == 1:
            print('Your current balance is:', Bank_Balance.amount)
        elif option == 2:
            user_ac = int(input('Enter amount to Withdraw: '))
            if user_ac > Bank_Balance.amount:
                print('Insufficient balance.')
            else:
                bank_balance = Bank_Balance.amount - user_ac
                with open('Bank_Balance.py', 'w') as file:
                    file.write(f'amount = {bank_balance}\n')
                print('Withdrawal successful. Your new balance is:', bank_balance)
        
        elif option == 3:
            print('Transaction ended.')
        
        else:
            print('Invalid option.')
    else:
        print('Wrong Pin')
else:
    print('Invalid Card')
