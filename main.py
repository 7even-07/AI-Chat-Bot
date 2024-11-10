



import json
from difflib import get_close_matches
from typing import Optional

# Load knowledge base from json file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Save the knowledge base back to the json file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find the best match for the user's question
def find_best_match(user_question: str, questions: list[str]) -> Optional[str]:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get the answer for the matched question
def get_answer_for_question(question: str, knowledge_base: dict) -> Optional[str]:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None



def chat_bot():
    knowledge_base = load_knowledge_base(r'C:\Users\Admin\Desktop\whatever\AI BOT\knoledge_base.json')

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Seven: Goodbye!")
            break

        if not user_input:
            print("Seven: Please ask a question or type 'quit' to exit.")
            continue

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base['questions']])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Seven: {answer}')
        else:
            print('Seven: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "Skip" to skip: ').strip()

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base(r'C:\Users\Admin\Desktop\whatever\AI BOT\knoledge_base.json', knowledge_base)
                print('Seven: Thank you! I learned a new response!')

if __name__ == '__main__':
    chat_bot()
