while True:
    Principal =float(int(input("Enter principal amount=>")))
    Rate_of_interest = float(int(input("Enter Interest_rate=>")))
    Total_Times_pan =float( int(input("Enter Total_span=>")))
    Number_of_time = float(int(input('Enter Number_of time=>')))


    Compound_interest = Principal*(1+((Rate_of_interest/180)*Number_of_time))**Number_of_time*Total_Times_pan
 
    if Compound_interest < 1000:
        print("you can withdraw from GHC and above")
    else:
        print('Transation Successfully')