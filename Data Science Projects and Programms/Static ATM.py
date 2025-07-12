print("\t\t\t\t\t\twelcome to HDFC ATM")
amount=1234567
pin=1234
if 'card'==input('Insert your card'):
    print('\t\t\t\t\t\twelcome')
    if pin==int(input("Enter your pin")):
        print("\t\t\t\t\t\t\t1)check balance\n\t\t\t\t\t\t\t2)cash withdraw")
        option=int(input('select your option'))
        if option==1:
            print("your current balance is :-", amount)
        elif option==2:
            user_amount=int(input('enter your amount'))
            print('your balance is :-',amount-user_amount)
    else:
        print("wrong pin")
else:
    print("Invalid card")