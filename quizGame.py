# BASIC QUIZ GAME
print("Welcome to Basics of Mathematics Quiz!")

play = input("Do you want to play? Type 'Y' for Yes or 'N' for No. ")

if play.upper() != 'Y':
    quit()

print("\nNote: You have to write the correct values from the options, not the option like A or B or C or D.")
print("Now, Let's Start the Quiz!")
score  = 0

ques = int(input("Q1) What is the sum of 130 + 125 + 191? A. 335 B. 456 C. 446 D. 426\n"))
if ques == 446:
    score = score + 1

ques = int(input("Q2) If we subtract 712 from 1500, what do we get? A. 788 B. 778 C. 768 D. 758\n"))
if ques == 788:
    score = score + 1

ques = int(input("Q3) 50 times 8 is equal to: A. 80 B. 400 C. 800 D. 4000\n"))
if ques == 400:
    score = score + 1

ques = int(input("Q4) 110 divided by 10 is: A. 11 B. 10 C. 5 D. 21\n"))
if ques == 11:
    score = score + 1

ques = int(input("Q5) 20 + (90 ÷ 2) is equal to: A. 50 B. 55 C. 65 D. 60\n"))
if ques == 65:
    score = score + 1

ques = int(input("Q6) The product of 82 and 5 is: A. 400 B. 410 C. 420 D. 480\n"))
if ques == 410:
    score = score + 1

ques = int(input("Q7) Find the missing term in the sequence: 3, 6, 9, __, 15. A. 10 B. 11 C. 12 D. 13\n"))
if ques == 12:
    score = score + 1

ques = int(input("Q8) Solve 24 ÷ 8 + 2. A. 5 B. 6 C. 8 D. 12\n"))
if ques == 5:
    score = score + 1

ques = int(input("Q9) Solve: 300 - (150 x 2)? A. 150 B. 100 C. 50 D. 0\n"))
if ques == 0:
    score = score + 1

ques = int(input("Q10) The product of 121 x 0 x 200 x 25 is: A. 1500 B. 0 C. 4000 D. 4200\n"))
if ques == 0:
    score = score + 1

percentage_obtained = (score/10) * 100

#print("Your final score is: " + str(score) + " out of 10.")
print(f"Your final score is: {score} out of 10.")
print(f"You obtained a percentage of {percentage_obtained}")
