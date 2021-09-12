#get user to choose a number (1-3)
number = input("Choose 1,2 or 3")
if number == 1 or number == 2 or number ==3:
     print("You have selected option number", number)
else:
    while number != 1 and number!=2 and number != 3:
        number = input("Choose 1,2 or 3")
    #endwhile
    print("You have selected option number", number)
#endif


    
   
