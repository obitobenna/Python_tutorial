day_num = int(input("what is today's date"))

if day_num == 1:
    print(" you chose Monday")
elif day_num ==2:
    print("you chose Tuesday")    
elif day_num ==3:
    print("you chose Wednesday")  
elif day_num ==4:
    print("you chose Thursday")  
elif day_num ==5:
    print("you chose Friday")  
elif day_num ==6:
    print("you chose Saturday")  
elif day_num ==7:
    print("you chose Sunday")    
else:
    print(" Error...Number does not exist ")    


grade_num= int(input(" user's grade "))   

if grade_num >= 90 and grade_num <= 100:
    print("A")
elif grade_num >= 80 and grade_num <= 89:
    print("B")    
elif grade_num >= 70 and  grade_num <= 79:
    print("C")    
elif grade_num >=60 and grade_num <= 69:
    print("D")
elif grade_num >=0 and grade_num <= 59:
    print("F")   
else:
    print ("invalid score")    
