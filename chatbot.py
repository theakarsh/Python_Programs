# Rule Based Chatbot

import datetime

name = input("Enter your Name : ")
presentTime = datetime.datetime.now().hour
if 5<= presentTime <=11 :
    print(f"Good Morning, {name}. Welcome to your Study Buddy ChatBot.")
elif 11<= presentTime <= 17 :
    print(f"Good Afternoon, {name}. Welcome to your Study Buddy ChatBot.")
elif 17<= presentTime <= 20:
    print(f"Good Evening, {name}. Welcome to your Study Buddy ChatBot.")
else:
    print(f"Good Night, {name}. Welcome to your Study Buddy ChatBot.")

print("You can ask me basic questions, Type 'bye' to exit.")

# Chatbot memory creation [Dictionary of responses]
responses = {
    "hello": "Hi, WELCOME. How can I help you?",
    "how are you": "I am very fine. Thank you.",
    "who are you": "I am Smart AI chatbot",
    "motivate me": "Just Keep going. Every bug makes makes you a better developer.",
    "happy": "Great to hear that",
    "what are functions": "Functions in Python are named blocks of reusable code designed to perform a specific task. They enhance code organization, readability, and reduce repetition.",
    "bye": "Exited Successfully. Thank you for using ChatBot."
}
# Function to get response of Chatbot 
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in  responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "Your question is out of my Memory Dataset."
    
# Take User Input and respond accordingly
while True:
    userInput = input("Ask your Question : ")
    reply = getResponseOfBot(userInput)
    print(f"Bot Response : {reply}")

    if "bye" in userInput.lower():
        break