pin = 1234
i=1
while i<=3:
    user_pin = int(input('Enter your pin =>'))
    if user_pin == pin:
        print('you have sucessfully logged in')
        i+=4
    elif user_pin != pin:
        if i==1:
            print(f"you have {3-1} attempts left")
        elif i == 2:
            print(f"you have{3-i} attempts left")
        else:
            print('you entered wrong pin 3 times')
    i+=1