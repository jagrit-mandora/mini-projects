questions=("Entomology is the science that studies: ",
           "Eritrea, which became the 182nd member"+
           " of the UN in 1993, is in the continent of: ",
           "Garampani sanctuary is located at: ",
           "For which of the following" +
           " disciplines is Nobel Prize awarded?")

options=(("A.Behavior of human beings", "B.Insects",
          "C.The origin and history of technicalscientific terms",
          "D.The formation of rocks"),
         ("A.Asia","B.Africa","C.Europe","D.Australia"),
         ("A.Junagarh, Gujarat","B.Diphu, Assam","C.Kohima, Nagaland","D.Gangtok, Sikkim",),
         ("Physics and Chemistry","Physiology or Medicine",
          "Literature, Peace and Economics","All of the above",))

user_answers=[]

correct_answer=("B","B","B","D")

acceptable_answer=("A","B","C","D")

question_number=0

score=0

for i in questions:
    print(i)
    print(options[question_number], end=" ")
    print()
    user_answer=input("enter the answer A,B,C,D: ").upper()
    if user_answer in acceptable_answer:
        user_answers.append(user_answer)
        if user_answer==correct_answer[question_number]:
            print("CORRECT ANSWER")
            score+=1
        else:
            print("INCORRECT ANSWER")
    else:
        print("INVALID OUTPUT")
        continue
    question_number += 1

print("----RESULT----")
print(f"CORRECT ANSWERS :{score} out of {len(questions)}")
print(f"SCORE :{(score/len(questions))*100}%")

