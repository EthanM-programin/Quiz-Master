# main.py - Core game logic engine.
from questions import QUIZ_QUESTIONS

def run_quiz():
    score = 0
    total_questions = len(QUIZ_QUESTIONS)

    print("Welcome to the Python Quiz!")

    # Loop through each question in the dictionary
    for index, q in enumerate(QUIZ_QUESTIONS, start=1):
        print(f"\nQuestion {index} of {total_questions}:")
        print(q["prompt"])

        # Print options for the current question
        for option in q["options"]:
            print(option)

        # Get user input and sanitize it (strip whitespace, convert to uppercase)
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Evaluate answer
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer'].upper()}.")

    # Final score output
    print(f"\nQuiz completed! Your final score is {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"Accuracy: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent work! You got a perfect score.")
    elif percentage >= 70:
        print("Solid performance. You passed the quiz, keep up the studying.")
    else:
        print("Good attempt, make sure to review the material and try again.")

if __name__ == "__main__":
    run_quiz()