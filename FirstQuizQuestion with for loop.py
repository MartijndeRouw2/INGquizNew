import random  #just because I wanted to use the random functionality

# counters set to 0, these will be raised after each question
questions_answered = 0
questions_correct = 0


# below are all the questions of this quiz and the answers
newquestions = {
    "1. In which year did NMB Postbank Groep and the insurance business of Nationale-Nederlanden merge to create ING Group?\n": "1991",
    "2. Does ING have a presence in Zimbabwe? \nYes or No\n": "No",
    "3. Since which year is Ralph Hamers CEO of ING Group?\n": "2013",
    "4. Lately there were rumours in the media about a merger between ING and a German bank. Which German bank?\n": "Commerzbank",
    "5. What is the monthly price of the OranjePakket in the Netherlands in €?\n": "1,55",
    "6. Guess a random number between 1-3\n": str(random.randint(1, 3)),  #had to make the random integer a string to compare with user input
    "7. In which city is ING Group headquartered?\n": "Amsterdam"}

# the following code will go through all questions and raise the counters
for question in newquestions:
    questions_answered += 1
    answer = input(question).capitalize()   #added .capitalize() so the answer is also correct if user forgot to capitalize the answer
    if answer == newquestions[question]:
        print("Correct!")
        questions_correct += 1
        print("You answered", questions_correct, "out of", questions_answered, "correct!\n")

    else:
        print("Wrong")
        print("You answered", questions_correct, "out of", questions_answered, "correct!\n")
input("This is the end of the quiz.")
