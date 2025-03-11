def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "In which movie did Leonardo DiCaprio win his first Oscar?",
            "options": ["A) The Revenant", "B) Inception", "C) Titanic", "D) The Wolf of Wall Street"],
            "answer": "A"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "answer": "B"
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["A) Python", "B) Java", "C) HTML", "D) C++"],
            "answer": "C"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your total score: {score} out of {len(questions)}")

if __name__ == "__main__":
    while True:
        quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break