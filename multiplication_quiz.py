import pyinputplus as pyip   
import time , random
no_of_questions = 10
correct_Answers = 0
for questionNo in range(no_of_questions):
    num01= random.randint(0,9)
    num02 = random.randint(0,9)
    prompt = "#%s : %s X %s = "%(questionNo,num01,num02)
    try:
        pyip.inputStr(prompt , allowRegexes=['^%s$'%(num01* num02)],blockRegexes=['.*','Incorrect Answer'],timeout= 5,limit= 2)
    except pyip.TimeoutException:
        print("Out of time")
    except pyip.RetryLimitException:
        print("Out of Chances")
    else:
        print("Correct!!")
        correct_Answers += 1
    
    time.sleep(1)
print("Correct Answers = {} , Incorrect Answers = {} ".format(correct_Answers,no_of_questions-correct_Answers))        
    