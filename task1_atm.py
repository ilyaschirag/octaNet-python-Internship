import time

# program will automatically run without entering the card after 5 seconds
print("please insert your card")

# this function is used to add delay for 5 seconds
time.sleep(5)

# this is the user pin
password=123027

#this is used to take user pin as input 
pin=int(input("please enter your pin: "))

#balance variable is used used to store the user account balance
balance=20000

# here is the condition if the entered pin by user is equal to the password only then the user cans see further options
if(password==pin):
    print("""
          1== balance
          2== withdrawn balance
          3== deposite balance
          4== exit
          """)
    
    try:
        option=int(input("please enter your choice: "))
    except:
        print("please enter valid option: ")

    # if user select 1 then the user can see their balance
    if(option==1):
        print(f'your balane is {balance}')
    
    # if user select 2 then the user can withdraw entered amount from his existing balance
    if(option==2):
        amount=int(input("enter amount: "))
        balance-=amount
        print("Transaction Successfull")
        print(f'your balane is {balance}')

    # if user select 3 then the user can deposit entered amount from his existing balance

    if(option==3):
        amount=int(input("enter amount: "))
        print("please insert cash")
        balance+=amount
        print(f'{amount} is successfully credit to your account')
        print(f'your updated balance is {balance}')

    if(option==4):
        exit


else:
    print("wrong pin")