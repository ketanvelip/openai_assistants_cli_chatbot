# assistant/openai_assistant.py
from openai import OpenAI
from dotenv import load_dotenv
import os

class OpenAIAssistant:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)
        self.assistant = self.get_set_assistant()
        self.thread = self.get_or_create_thread()

    def get_set_assistant(self):
        assistant_id = None
        try:
            with open('assistant_id.txt', 'r') as file:
                assistant_id = file.read().strip()
                if not assistant_id:
                    raise ValueError("Assistant ID file is empty")
                assistant = self.client.beta.assistants.retrieve(assistant_id)
                print(f"Using existing assistant with ID: {assistant_id}")
                return assistant
        except (FileNotFoundError, ValueError):
            assistant = self.client.beta.assistants.create(
                name="Personal Assistant - Ketan",
                instructions="You are a personal assistant to answer user queries.",
                tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
                model="gpt-4o",
            )
            with open('assistant_id.txt', 'w') as file:
                file.write(assistant.id)
                print(f"Created new assistant with ID: {assistant.id}")
            return assistant

    def get_or_create_thread(self):
        try:
            with open('thread_id.txt', 'r') as file:
                thread_id = file.read().strip()
                if not thread_id:
                    raise ValueError("Thread ID file is empty")
                thread = self.client.beta.threads.retrieve(thread_id)
                print(f"Using existing thread with ID: {thread_id}")
                return thread
        except (FileNotFoundError, ValueError):
            thread = self.client.beta.threads.create()
            with open('thread_id.txt', 'w') as file:
                file.write(thread.id)
                print(f"Created new thread with ID: {thread.id}")
            return thread

    def get_response(self, prompt):
        message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=prompt
        )

        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            # instructions="Please address the user as Jane Doe. The user has a premium account." # add instructions if required
        )

        if run.status == 'completed': 
            messages = list(self.client.beta.threads.messages.list(
                thread_id=self.thread.id,
                run_id=run.id
            ))
            return messages[0].content[0].text.value