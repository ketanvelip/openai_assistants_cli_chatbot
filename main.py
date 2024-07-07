# main.py
from assistant.openai_assistant import OpenAIAssistant

def main():
    openai_assistant = OpenAIAssistant()
    while True:
        user_prompt = input("\nEnter your prompt: ")
        if user_prompt.lower() in ["exit", "quit"]:
            break
        response = openai_assistant.get_response(user_prompt)
        print("\nResponse: ", response)

if __name__ == "__main__":
    main()
