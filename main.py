# main.py - Core game logic engine with JSON score persistence.
import json
import os
from questions import QUIZ_QUESTIONS

SCORES_FILE = "score.json"

def load_leaderboard():
    """Load past scores from the JSON file if it exists."""
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_and_display_leaderboard(player_name, score, total):
    """Save the current score JSON, sort leaderboard, and display top scores."""
    leaderboard = load_leaderboard()

    percentage = (score / total) * 100
    leaderboard.append({
        "name": player_name,
        "score": score,
        "total": total,
        "percentage": percentage
    })

    # Sort leaderboard by percentage in descending order (highest first)
    leaderboard = sorted(leaderboard, key=lambda x: x["percentage"], reverse=True)

    # Save back to JSON file with indentation for readability
    with open(SCORES_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)

    print("\n All-Time Leaderboard:")
    # Display top 5 scores using list slicing [:5]
    for i, entry in enumerate(leaderboard[:5], start=1):
        print(f"{i}. {entry['name']} - {entry['score']}/{entry['total']} ({entry['percentage']:.1f}%)")

def run_quiz():
    score = 0
    total_questions = len(QUIZ_QUESTIONS)

    print("Welcome to the Python Quiz!")

    player_name = input("Enter your coder tag / name: ").strip()
    if not player_name:
        player_name = "Anonymous Coder"

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

    # Save and display leaderboard stats
    save_and_display_leaderboard(player_name, score, total_questions)

if __name__ == "__main__":
    run_quiz()