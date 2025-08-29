# Quiz Game

lst = ['a', 'b', 'c', 'd']

def question1():
    print("\n1. Who is the current President of the United States (in 2025)?")
    print("a) Joe Biden\nb) Donald Trump\nc) Ron DeSantis\nd) Kamala Harris")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "a":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question2():
    print("\n2. Which country hosted the 2024 Summer Olympics?")
    print("a) Japan\nb) France\nc) USA\nd) China")
    answer = input("Your answer: ").strip().lower()
    if answer == "a" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "b":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question3():
    print("\n3. What is the most followed account on Instagram in 2025?")
    print("a) Cristiano Ronaldo\nb) Lionel Messi\nc) Kylie Jenner\nd) Instagram itself")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "a":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question4():
    print("\n4. Which tech company launched the AI model called 'Gemini'?")
    print("a) Microsoft\nb) OpenAI\nc) Google\nd) Meta")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'a' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "c":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question5():
    print("\n5. Which movie won the Best Picture Oscar in 2025?")
    print("a) Oppenheimer\nb) Poor Things\nc) Barbie\nd) Everything Everywhere All at Once")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "a":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question6():
    print("\n6. What is the name of the ongoing conflict between Russia and Ukraine?")
    print("a) Crimean War\nb) Russo-Ukrainian War\nc) Eastern Conflict\nd) NATO-Ukrainian Crisis")
    answer = input("Your answer: ").strip().lower()
    if answer == "a" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "b":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question7():
    print("\n7. Which team won the UEFA Euro 2024?")
    print("a) England\nb) Germany\nc) Spain\nd) France")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'a' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "c":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question8():
    print("\n8. Which company became the first to reach a $4 trillion market cap?")
    print("a) Apple\nb) Microsoft\nc) Amazon\nd) Nvidia")
    answer = input("Your answer: ").strip().lower()
    if answer == "a" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "b":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question9():
    print("\n9. Who won the Ballon d'Or in 2024?")
    print("a) Lionel Messi\nb) Kylian Mbappé\nc) Erling Haaland\nd) Jude Bellingham")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "a":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


def question10():
    print("\n10. Which app surpassed TikTok in global downloads in 2025?")
    print("a) Threads\nb) YouTube Shorts\nc) Instagram\nd) CapCut")
    answer = input("Your answer: ").strip().lower()
    if answer == "b" or answer == 'c' or answer  == 'd':
        print("-------Wrong Answer😞-------")
    if answer == "a":
        print("-------Correct Answer🥳-------")
    elif answer not in lst:
        print("Invalid choice")


questions = {
    1: question1,
    2: question2,
    3: question3,
    4: question4,
    5: question5,
    6: question6,
    7: question7,
    8: question8,
    9: question9,
    10: question10
}

available = list(questions.keys())

print('----------Welcome to the Quiz----------')

while available:
    print('\nAvailable questions', available)

    try:
        choice = int(input("Please select a question number: "))

        if choice in available:
            questions[choice]()
            available.remove(choice)
        
        else:
            print("That question is not available. Choose again.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

print('You have answered all question\nQuiz is over')

