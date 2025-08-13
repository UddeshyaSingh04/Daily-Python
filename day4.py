# Who want to be billionaier (KAUN BANEGA COROEPATTI)

questions = [
    ["who is sharukh Khan", "WWE Wrestler", "Plumber","Actor", "Astronut", 3],
    ["What is the capital of France?", "Berlin", "Madrid", "Rome", "Paris", 4],
    ["Which planet is known as the Red Planet?", "Earth", "Jupiter", "Venus", "Mars", 4],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "Jane Austen", "Mark Twain", "William Shakespeare", 4],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Iron", "Carbon", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Rhino", 1],
    ["Who painted the Mona Lisa?", "Van Gogh", "Michelangelo", "Pablo Picasso", "Leonardo da Vinci", 4],
    ["Which programming language is known for web development?", "Python", "C++", "HTML", "JavaScript", 3],
]

prize = [1000, 10000, 100000, 1000000, 1000000, 10000000, 100000000, 1000000000]
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer is correct or not

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d: "))
    if(question[5] == a):
        print("Correct Answer")

    else:
        print(f"Incorrect, Correct answer was {question[5]}")
        print("Better Luck next time!")
        break

    print(f"You Won {prize[i]}")
    i += 1
