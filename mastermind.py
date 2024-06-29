import random
num=random.randrange(1000,10000)
chances=5
guess=int(input("guess a 4 digit number :"))
if guess==num:
    print("great! you guessed it in your first attempt, now you are a mastermind")
else:
    tries=0
    while guess!=num and chances:
        tries=tries+1
        chances=chances-1
        count=0
        guess=str(guess)
        num=str(num)
        correct=['*']*4
        for i in range(0,4):
            if guess[i]==num[i]:
                count=count+1
                correct[i]=num[i]
            else:
                continue
        if count<4 and count>0 and chances:
            print("not a correct guess, but you guessed",count, "numbers correctly")
            print("current status is:")
            for char in correct:
                  print(char, end=' ')
            print('\n')
            print('\n')
            guess=int(input("guess a 4 digit number" ))
            print("you have", chances, "chances left" )
        elif count==0 and chances:
                  print("none of the digits you guessed is right")
                  guess=int(input("guess a 4 digit number "))
                  print("you have " ,chances, "chances left")

    if guess==num:
        print("great ! you won in ", tries, "guessess now you are a mastermind")
    if chances==0:
        print("sorry, you lost ,as you ran out of chances")
        print("number is ",num)
                  
       
            
        
        
    
