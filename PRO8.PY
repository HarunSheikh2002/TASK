def Question1():
    Question1="Q1. which language is used to create facebook?"
    option="1)python" , "2)french", "3)javascript", "4)php"
    print(Question1)
    print(option)
    ans=input("Enter you answer:-")
    if ans=="php":
        print("Right answer")
    else:
        print("Wrong answer.") 

def Question2():
    Question2="Q2. which one is not feature of python language"
    option = "1)interpreted","2)portable","3)high levl ", "4)case insensitive"
    print(Question2)
    print(option)
    ans=input("Enter your answer:-")
    if ans=="case insensitive":
        print("Right answer")
        
    else:
        print("Wrong answer")

def Question3():
    Question3="Q3. the command used to start python from the command prompt is ______"
    option = "1)execute python", "2)python", "3)py", "4)both 2 and 3 are correct"
    print(Question3)
    print(option)
    ans=input("Enter your answer:")
    if ans=="both 2 and 3 are correct":
        print("Right answer")
    else:
        print("Wrong answer.")
    
def Question4():
    Question4="Q4. How many states are there in INDIA?"
    option = "1)28","2)34","3)23","4)27"
    print(Question4)
    print(option)
    ans=int(input("Enter your answer:"))
    if ans=="28":
        print("Right answer")
    else:
        print("Wrong answer.")
    

def Question5():
    Question5="Q5. which city  is capital of india ?"
    option= "1)pune","2)delhi","3)mumbai","4)nagpur"
    print(Question5)
    print(option)
    ans=(input("Enter your answer:"))
    if ans=="delhi":
        print("Right answer")
    else:
        print("Wrong answer.")
    
def Question6():
    Question6="Q6. which of following is keyword used in python?"
    option = "1) finally", "2)lambda", "3)for","4)all of above"
    print(Question6)
    print(option)
    ans=input("Enter your answer :")
    if ans == "4)all of above":
        print("Rigth answer ")
    else:
        print("Wrong answer")

def Question7():
    Question7="Q7. what is the maximum length of a python identifier?"
    option = "1)33", "2)28", "3)14", "4)no fixed length specified"
    print(Question7)
    print(option)
    ans=input("Enter your answer :")    
    if ans=="no fixed length specified":
        print("Right answer")
    else:
        print("Wrong answer")

def Question8():
    Question8="Q8. who is current prime minister of india ?"
    option= "1)narendra modi","2)rabindranath tagor","3)ashok gehlot"
    print(Question8)
    print(option)
    ans=input("Enter your answer :")
    if ans == "narendra modi":
        print("Right answer ")
    else:
        print("Wrong answer")


status = True
while status:
    choice = int(input("enter your choice :"))
    if choice == 1:
        Question1()
    elif choice == 2:
        Question2()
    elif choice == 3:
        Question3()
    elif choice == 4:
        Question4()
    elif choice == 5:
        Question5()
    elif choice == 6:
        Question6()
    elif choice == 7:
        Question7()
    elif choice == 8:
        Question8()



    main_choice = input("countinue for yes :")
    if main_choice == 'y':
        status = True
    else:
        status = False
