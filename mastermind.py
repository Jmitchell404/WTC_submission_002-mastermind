import random


def run_game():
#step1
    digit_list = list()                         #converts the digit_list into a list
    while len(digit_list) !=4:                  #the length must be 4 digits
        random_digit = random.randint(1, 8)     #randomly chosen 4 digits between the range of 1 to 8
        if random_digit not in digit_list:      #makes sure that the randomly chosen 4 digits are in the digit list
            digit_list.append(random_digit)

    print("4-digit Code has been set. Digits in range 1 to 8.",
    "You have 12 turns to break it.")
#step2
    guess = 12
    while guess > 0:
        user_input = input("Input 4 digit code: ")
        if user_input.isnumeric and len(user_input) == 4: #only accpets the user's input as digits and 4 digits in length 
            user_input = list(user_input)                 #the user input is turned into a list
            for pos, val in enumerate(user_input):        #pos is checking if the position of each individual digit is correct
                int_val = int(val)                        #val is checking if the digit is the corrct value for each individual value
                user_input[pos] = int_val
                if not (0 < int_val < 9):                 #if the value is`nt in range of 1-8 then it will print out,
                    print("Please enter exactly 4 digits.") #Please enter exactly 4 digits. and shows to input another value   
                    break
        else:
            print("Please enter exactly 4 digits.")
            continue
#step3 and step4
        correct_place = 0
        wrong_place = 0
        guess -= 1       #subtracts a guess each time there is a wrong input
        for i in range(4): #checks all 4 randomly generated digits
            if user_input[i] == digit_list[i]: # checks the digit list for both the position and calue of all 4 digits
                correct_place += 1
            elif user_input[i] in digit_list:
                wrong_place += 1
        
        print("Number of correct digits in correct place:    ", correct_place)
        print("Number of correct digits not in correct place:", wrong_place) 
 
        if user_input == digit_list:
            print("Congratulations! You are a codebreaker!\nThe code was:", 
            f"{digit_list[0]}{digit_list[1]}{digit_list[2]}{digit_list[3]}")
            break
        print("Turns left:",guess)
       


if __name__ == "__main__":
    run_game()
