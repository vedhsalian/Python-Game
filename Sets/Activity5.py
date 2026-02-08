correct_answers={"144","Africa","Equator"}
answers=set()

Q1=int(input("What is 12x12? "))

Q2=input("What continent is Egypt in? ")

Q3=input("What is the imaginary line that runs down the center of the Earth? ")

answers={Q1,Q2,Q3}

answered_correct=correct_answers&answers
correct=len(answered_correct)

print("You answered "+str(correct)," questions correctly!")