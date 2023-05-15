print("---------------------------------------------------------")
print("----------------Guessing A Number Start -----------------")
print("---------------------------------------------------------")

guess_number = 100
input_number = 0
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess_number != input_number and not out_of_guesses:
    if guess_count == 0:
        input_number = int(input("Enter a Number. You have " + str(guess_limit - guess_count) + " chances: "))
    else:
        if input_number > guess_number:
            input_number = int(
                input("Enter a Smaller Number. You only have " + str(guess_limit - guess_count) + " chances: "))
        elif input_number < guess_number:
            input_number = int(
                input("Enter a Bigger Number. You only have " + str(guess_limit - guess_count) + " chances: "))
    if guess_count == guess_limit:
        out_of_guesses = True
    guess_count += 1

if out_of_guesses:
    print("Out of Guesses, You lose!")
else:
    print("The Guessing Number is " + str(guess_number) + ". You win!")

print("---------------------------------------------------------")
print("----------------Guessing A Number End -----------------")
print("---------------------------------------------------------")
