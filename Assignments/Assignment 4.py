while True:
    Enter_grade = float(int(input("Enter grade value -")))
    if 0>=  Enter_grade <40:
        print('pass')
    elif 40 >= Enter_grade < 50:
        print('third class lower')
    elif  50 >=  Enter_grade < 60:
        print('second class lower')
    elif  60 >=  Enter_grade < 70:
        print('second class upper')
    elif  70 >=  Enter_grade < 100:
        print('first class lower')
    else:
        print('you entered a wrong input')