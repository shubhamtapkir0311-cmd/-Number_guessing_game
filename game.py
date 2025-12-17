import random

low = 1
high = 50

print("machine is geassing your number between 1 to 50..")

while True:
    guess = (low + high) // 2
    
    print(" machine  guesses:" ,guess)
    number= input(" Enter your Option\n 1. Number is Correct \n 2. number is High From my number \n 3. Number Low from my Number : ")
    if number  == "1":
      print("\n machine successfully guest your number : ",guess)
      print("\n")
      break
    elif number == "2":
        high = guess - 1
    elif number == "3":
        low = guess + 1
    else:
        print("\n  you Enter wrong input ")
        