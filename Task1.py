class SimpleChatbot:
    def __init__(self):
        self.user_name = None  

    def respond(self, user_input):
        user_input = user_input.lower()  
        
        
        if "hi" in user_input or "hello" in user_input or "hey" in user_input:
            if self.user_name:
                return f"Hi again, {self.user_name}! How can I assist you?"
            return "Hello! I'm a chatbot. What's your name?"

        
        elif "my name is" in user_input:
           
            name = user_input.split("my name is")[-1].strip()
            if name:
                self.user_name = name.capitalize()
                return f"Nice to meet you, {self.user_name}! How can I help you?"
            return "I didn't catch your name. Could you please repeat?"

        
        elif "what time" in user_input or "current time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            return f"The current time is {current_time}."

        
        elif "who are you" in user_input or "your name" in user_input:
            return "I'm a simple chatbot created to assist you with basic queries."

        
        elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
            if self.user_name:
                return f"Goodbye, {self.user_name}! Have a great day!"
            return "Goodbye! Take care!"

        
        elif "help" in user_input:
            return """I can help you with:
- Saying hello
- Telling the time
- Answering basic questions
- You can introduce yourself by saying 'My name is ...'"""

        
        else:
            return "I'm not sure how to respond to that. Try typing 'help' to see what I can do!"


def main():
    chatbot = SimpleChatbot()
    print("Chatbot: Hi! I'm a chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip()  
        if "exit" in user_input.lower():  
            print("Chatbot:", chatbot.respond("exit"))
            break
        print("Chatbot:", chatbot.respond(user_input)) 

if __name__ == "__main__":
    main()
